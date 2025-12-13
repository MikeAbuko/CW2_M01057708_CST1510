# Week 10 - AI Service
# Simple functions to use Hugging Face AI

import streamlit as st
from huggingface_hub import InferenceClient


def get_hf_client():
    """
    Connect to Hugging Face AI
    
    Returns:
        InferenceClient - connection to AI
    """
    # Get API token from secrets file
    token = st.secrets["HF_TOKEN"]
    
    # Create AI client
    client = InferenceClient(token=token)
    
    return client


def analyze_security_incident(incident_description):
    """
    Use AI to analyze a security incident
    
    Parameters:
        incident_description (str) - what happened in the incident
        
    Returns:
        str - AI analysis with recommendations
    """
    try:
        # Get AI client
        client = get_hf_client()
        
        # Create message for AI
        messages = [
            {
                "role": "user",
                "content": f"""You are a senior cybersecurity analyst expert. Analyze this security incident:

Incident: {incident_description}

Provide a brief analysis including:
1. Threat Level (Low/Medium/High/Critical)
2. Attack Type
3. Recommended Actions (2-3 steps)

Keep your response concise and professional adhering to the best practices and modern technologies."""
            }
        ]
        
        # Ask AI using chat - using free Llama model
        response = client.chat_completion(
            messages=messages,
            model="meta-llama/Llama-3.2-3B-Instruct",
            max_tokens=300,
            temperature=0.7
        )
        
        # Get the answer from AI response
        answer = response.choices[0].message.content
        return answer
        
    except Exception as e:
        return f"Error analyzing incident: {str(e)}"


def generate_security_tips():
    """
    Get security tips from AI
    
    Returns:
        str - list of 5 security tips
    """
    try:
        # Get AI client
        client = get_hf_client()
        
        # Create message for AI
        messages = [
            {
                "role": "user",
                "content": """You are a senior cybersecurity analyst expert. Provide 5 key cybersecurity best practices for 2025 or the latest date trends.

Format as a numbered list (1-5). Keep each point brief and actionable."""
            }
        ]
        
        # Ask AI - using free Llama model
        response = client.chat_completion(
            messages=messages,
            model="meta-llama/Llama-3.2-3B-Instruct",
            max_tokens=250,
            temperature=0.7
        )
        
        # Get answer
        answer = response.choices[0].message.content
        return answer
        
    except Exception as e:
        return f"Error generating tips: {str(e)}"


def chat_with_ai(user_question):
    """
    Chat with AI about cybersecurity
    
    Parameters:
        user_question (str) - question to ask AI
        
    Returns:
        str - AI's answer
    """
    try:
        # Get AI client
        client = get_hf_client()
        
        # Create message for AI
        messages = [
            {
                "role": "user",
                "content": f"""You are a helpful senior cybersecurity analyst assistant who follows up on the most current trends. Answer this question clearly and concisely.

Question: {user_question}

Answer:"""
            }
        ]
        
        # Ask AI - using free Llama model
        response = client.chat_completion(
            messages=messages,
            model="meta-llama/Llama-3.2-3B-Instruct",
            max_tokens=300,
            temperature=0.7
        )
        
        # Get answer
        answer = response.choices[0].message.content
        return answer
        
    except Exception as e:
        return f"Error: {str(e)}"
