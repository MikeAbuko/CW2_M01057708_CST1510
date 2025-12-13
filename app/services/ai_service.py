# Week 11 - AI Service with Multiple Companies
# AI Assistant class that works with multiple AI services for speed and current info
# Uses: HuggingFace (backup), Groq (fast), and SerpAPI (web search)

import streamlit as st
from huggingface_hub import InferenceClient

# Try to import optional AI providers
# If they're not installed or no API key, we just use HuggingFace
try:
    from groq import Groq
    GROQ_AVAILABLE = True
except ImportError:
    GROQ_AVAILABLE = False

try:
    from serpapi import GoogleSearch
    SERPAPI_AVAILABLE = True
except ImportError:
    SERPAPI_AVAILABLE = False


class AIAssistant:
    """
    A class to work with AI - Enhanced Version!
    
    This class can use three different AI services:
    1. HuggingFace - Always available (backup)
    2. Groq - Fast AI responses (optional)
    3. SerpAPI - Gets current information from web (optional)
    
    It automatically uses the best available service and falls back if needed
    """
    
    def __init__(self):
        """
        Constructor - set up all available AI services
        """
        # STEP 1: Set up HuggingFace (this always works)
        self.__hf_token = st.secrets["HF_TOKEN"]
        self.__hf_client = InferenceClient(token=self.__hf_token)
        self.__hf_model = "meta-llama/Llama-3.2-3B-Instruct"
        
        # STEP 2: Try to set up Groq (fast AI)
        # Groq is much faster than HuggingFace but needs an API key
        self.__groq_client = None
        if GROQ_AVAILABLE and "GROQ_API_KEY" in st.secrets:
            try:
                self.__groq_client = Groq(api_key=st.secrets["GROQ_API_KEY"])
                self.__groq_model = "llama-3.1-8b-instant" 
                print("✓ Groq API configured - fast responses enabled")
            except Exception as e:
                print(f"✗ Groq setup failed: {e}")
        else:
            print("ℹ Groq not configured - using HuggingFace only")
        
        # STEP 3: Try to set up SerpAPI (web search for current info)
        # This lets us search Google for latest threats and news
        self.__serpapi_key = None
        if SERPAPI_AVAILABLE and "SERPAPI_KEY" in st.secrets:
            self.__serpapi_key = st.secrets["SERPAPI_KEY"]
            print("✓ SerpAPI configured - web search enabled for current info")
        else:
            print("ℹ SerpAPI not configured - using training data only")
    
    def __get_current_threats(self, search_query):
        """
        HELPER METHOD: Search the web for current threat information
        (This is a private method - only used inside this class)
        
        Parameters:
            search_query (str) - what to search for on Google
            
        Returns:
            str - current information from web, or empty string if no API key
        """
        # If we don't have SerpAPI key, just return empty
        if not self.__serpapi_key:
            print("⚠️  SerpAPI key not configured - skipping web search")
            return ""
        
        try:
            # Search Google using SerpAPI
            search = GoogleSearch({
                "q": search_query,
                "api_key": self.__serpapi_key,
                "num": 5  # Get top 5 results
            })
            
            results = search.get_dict()
            
            # Check for errors
            if "error" in results:
                print(f"❌ SerpAPI error: {results['error']}")
                return ""
            
            # Extract useful info from search results
            current_info = []
            if "organic_results" in results:
                print(f"📰 Found {len(results['organic_results'])} search results")
                for result in results["organic_results"][:5]:
                    title = result.get("title", "")
                    snippet = result.get("snippet", "")
                    date = result.get("date", "")
                    link = result.get("link", "")
                    
                    if title and snippet:
                        # Include date and actual URL
                        entry = f"- {title}"
                        if date:
                            entry += f" ({date})"
                        entry += f": {snippet}"
                        if link:
                            entry += f"\n  Source: {link}"
                        current_info.append(entry)
            
            # Return the information we found
            if current_info:
                return "\n".join(current_info)
            else:
                print("⚠️  No organic results found in search")
                return ""
                
        except Exception as e:
            print(f"❌ Web search exception: {e}")
            return ""
    
    def __ask_ai(self, messages, use_web_search=False, search_query=None):
        """
        HELPER METHOD: Send question to AI (tries Groq first, then HuggingFace)
        (This is a private method - only used inside this class)
        
        Parameters:
            messages (list) - the conversation messages to send to AI
            use_web_search (bool) - should we add current web info?
            search_query (str) - what to search for if using web
            
        Returns:
            str - AI's response
        """
        # STEP 1: Add current web information if requested
        if use_web_search and search_query:
            print(f"🔍 Searching web: {search_query}")
            web_info = self.__get_current_threats(search_query)
            if web_info:
                # Add the web results to the USER message (last one in the list)
                # The system message is first, user message is last
                messages[-1]["content"] += f"\n\n## CURRENT WEB SEARCH RESULTS (Retrieved December 2025):\n{web_info}\n\n⚠️ MANDATORY INSTRUCTIONS:\n1. Write your professional analysis using the information above\n2. Keep URLs out of the main body\n3. At the END, add references section using this EXACT format:\n\n**References:**\n[1] Article Title - https://actual-url-from-source-line.com\n[2] Article Title - https://actual-url-from-source-line.com\n\nEXAMPLE (if search results showed 'Source: https://example.com/article'):\n**References:**\n[1] Cloudflare DDoS Report - https://example.com/article\n\n4. CRITICAL: Copy the EXACT URLs after 'Source:' in the results above\n5. If you write '[1] Title' without the actual URL, that is WRONG - always include the full URL"
                print("✓ Web search successful - added current info to prompt")
                print(f"📊 Added {len(web_info.split('- '))-1} search results to context")
            else:
                print("✗ Web search returned no results - check SerpAPI key or query")
        
        # STEP 2: Try Groq first since it's faster
        if self.__groq_client:
            try:
                response = self.__groq_client.chat.completions.create(
                    model=self.__groq_model,
                    messages=messages,
                    max_tokens=1000,
                    temperature=0.7
                )
                return response.choices[0].message.content
            except Exception as e:
                print(f"Groq failed, trying HuggingFace: {e}")
        
        # STEP 3: Use HuggingFace as backup since it will ideally always work
        try:
            response = self.__hf_client.chat_completion(
                messages=messages,
                model=self.__hf_model,
                max_tokens=1000,
                temperature=0.7
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Error: {str(e)}"
    
    def analyze_incident(self, incident_description):
        """
        Use AI to analyze a security incident with professional-grade analysis through enhanced prompting
        
        Parameters:
            incident_description (str) - what happened
            
        Returns:
            str - detailed AI analysis with expert recommendations
        """
        # Create a professional prompt
        # We tell the AI to act like a senior security expert
        messages = [
            {
                "role": "system",
                "content": """You are a Senior Cybersecurity Analyst with 15+ years of experience in incident response, threat intelligence, and security operations. Your expertise includes:
- Advanced persistent threats (APTs)
- Modern attack vectors and MITRE ATT&CK framework
- Zero-trust architecture and defense-in-depth strategies
- Incident response and forensic analysis
- Risk assessment and threat modeling"""
            },
            {
                "role": "user",
                "content": f"""Analyze the following security incident with professional rigor:

**INCIDENT DETAILS:**
{incident_description}

**REQUIRED ANALYSIS:**

1. **THREAT CLASSIFICATION**
   - Severity Level: [Critical/High/Medium/Low] with justification
   - Attack Vector: Primary method used
   - MITRE ATT&CK Mapping: Relevant technique IDs

2. **TECHNICAL ASSESSMENT**
   - Attack Type: Detailed categorization
   - Indicators of Compromise (IoCs): What to look for
   - Potential Impact: Business and technical consequences

3. **IMMEDIATE RESPONSE**
   - Containment Actions: 2-3 immediate steps
   - Investigation Priority: What to analyze first
   - Evidence Preservation: Critical data to secure

4. **STRATEGIC RECOMMENDATIONS**
   - Short-term remediation (24-48 hours)
   - Long-term security improvements
   - Similar attack prevention measures

Provide concise, actionable analysis with specific dates and recent examples where relevant."""
            }
        ]
        
        # Send to AI (uses Groq if available, otherwise HuggingFace)
        # No web search needed for incident analysis
        return self.__ask_ai(messages, use_web_search=False)
    
    def get_security_tips(self):
        """
        Get expert cybersecurity tips based on current threat landscape
        Uses web search to get latest threat information if available
        
        Returns:
            str - professional security recommendations
        """
        # Create a professional prompt
        # We tell the AI to act like a tech expert, CISO (Chief Information Security Officer)
        messages = [
            {
                "role": "system",
                "content": """You are a Chief Information Security Officer (CISO) advising on enterprise security strategy. You stay current on:
- Emerging threat actors and campaigns
- Zero-day vulnerabilities and exploit trends
- Security frameworks (NIST, ISO 27001, CIS Controls)
- Cloud security and DevSecOps practices
- Regulatory compliance (GDPR, SOC 2, etc.)

CRITICAL: When web search results are provided:
- Use the data and insights from sources in your main response
- DO NOT put URLs in the body - keep analysis clean and professional
- At the END, include a 'References:' section with the ACTUAL URLs from 'Source:' lines
- COPY the exact URLs - do not fabricate or write placeholder links"""
            },
            {
                "role": "user",
                "content": """Provide 5 critical cybersecurity best practices for modern organizations facing today's threat landscape.

**REQUIREMENTS:**
- Address current attack trends (ransomware, supply chain, cloud threats)
- Include specific technologies and methodologies
- Focus on practical, implementable strategies
- Consider resource constraints of real organizations
- Prioritize high-impact, cost-effective measures

**FORMAT:**
1. **[Practice Name]**: Brief description
   - Why it matters: Business impact (include recent statistics with dates)
   - How to implement: 2-3 concrete steps
   - Key technologies/tools: Specific examples

Avoid generic advice. Provide actionable, modern security guidance with specific dates and recent examples."""
            }
        ]
        
        # Send to AI with web search to get current threats
        return self.__ask_ai(
            messages,
            use_web_search=True,
            search_query="cybersecurity threats best practices 2025 prioritising info from cisoseries.com but not making it the only source as judge and jury"
        )
    
    def chat(self, user_question):
        """
        Expert cybersecurity consultation on any security topic
        Uses web search to provide current, accurate information
        
        Parameters:
            user_question (str) - question to ask
            
        Returns:
            str - expert analysis with current context
        """
        # Create a professional prompt
        # We tell the AI to act like a top security consultant
        messages = [
            {
                "role": "system",
                "content": """You are an senior elite cybersecurity consultant providing strategic advice to organizations. Your communication style is:
- Professional yet accessible
- Evidence-based and practical
- Aware of current threat intelligence
- Balanced between theory and real-world application
- Focused on risk management and business outcomes

You reference modern security concepts like zero-trust, SASE, XDR, SOAR, and cloud-native security and more without being overly technical.

CRITICAL: When web search results are provided:
- Use the information and dates from sources in your main analysis
- DO NOT include URLs in the body of your response
- At the END, add a 'References:' section
- Each reference MUST have the ACTUAL URL from the search results (look for 'Source: https://...')
- NEVER write fake URLs or placeholder text - ONLY use real URLs from search results"""
            },
            {
                "role": "user",
                "content": f"""**CONSULTATION REQUEST:**
{user_question}

**RESPONSE GUIDELINES:**
- Provide current, practical advice with specific dates when available
- Include specific examples from recent incidents and trends
- Consider both technical and business perspectives
- Suggest concrete next steps or resources
- Keep response focused and actionable
- Reference years and dates to demonstrate currency of information

Answer as if advising a client who needs clear, professional guidance."""
            }
        ]
        
        # Send to AI with web search to provide current context
        return self.__ask_ai(
            messages,
            use_web_search=True,
            search_query=f"{user_question} cybersecurity 2025"
        )


# BACKWARD COMPATIBILITY
# Old functions working so existing code doesn't break

def get_hf_client():
    """
    Old function - creates AI client (OLD WAY)
    Use AIAssistant class instead for new code
    """
    token = st.secrets["HF_TOKEN"]
    client = InferenceClient(token=token)
    return client


def analyze_security_incident(incident_description):
    """
    Old function - analyze incident (OLD WAY)
    Use AIAssistant().analyze_incident() for new code
    """
    ai = AIAssistant()
    return ai.analyze_incident(incident_description)


def generate_security_tips():
    """
    Old function - get tips (OLD WAY)
    Use AIAssistant().get_security_tips() for new code
    """
    ai = AIAssistant()
    return ai.get_security_tips()


def chat_with_ai(user_question):
    """
    Old function - chat with AI (OLD WAY)
    Use AIAssistant().chat() for new code
    """
    ai = AIAssistant()
    return ai.chat(user_question)
