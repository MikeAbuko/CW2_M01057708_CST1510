# Week 10 - AI Assistant Page
# Chat with AI about cybersecurity

import streamlit as st
from app.services.ai_service import generate_security_tips, chat_with_ai

# Page configuration
st.set_page_config(
    page_title="AI Assistant",
    page_icon="🤖",
    layout="wide"
)

# Check if user is logged in
if 'logged_in' not in st.session_state or not st.session_state.logged_in:
    st.error("🔒 Please login first!")
    st.info("👈 Go to Home page to login")
    st.stop()

# Page header
st.title("🤖 AI Security Assistant")
st.markdown("Get AI-powered cybersecurity advice and answers")

# Create tabs for different features
tab1, tab2 = st.tabs(["💬 Ask AI", "💡 Security Tips"])

# TAB 1: Chat with AI
with tab1:
    st.subheader("Ask Cybersecurity Questions")
    
    # Text box for user question
    user_question = st.text_area(
        "Your Question",
        placeholder="Example: What is a DDoS attack and how can I prevent it?",
        height=100
    )
    
    # Submit button
    if st.button("Ask AI", type="primary", use_container_width=True):
        if not user_question:
            st.error("❌ Please enter a question first!")
        else:
            with st.spinner("🤖 AI is thinking... This may take 10-20 seconds..."):
                # Get answer from AI
                answer = chat_with_ai(user_question)
            
            # Show the answer
            st.success("✅ AI Response:")
            st.info(answer)
    
    st.divider()
    
    # Quick question buttons
    st.markdown("#### ⚡ Quick Questions")
    st.markdown("Click these buttons for instant answers to common questions")
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("🔐 What is two-factor authentication?", use_container_width=True):
            with st.spinner("🤖 Thinking..."):
                answer = chat_with_ai("What is two-factor authentication and why is it important?")
                st.info(answer)
        
        if st.button("🛡️ What is a firewall?", use_container_width=True):
            with st.spinner("🤖 Thinking..."):
                answer = chat_with_ai("What is a firewall and how does it protect networks?")
                st.info(answer)
    
    with col2:
        if st.button("🎣 What is phishing?", use_container_width=True):
            with st.spinner("🤖 Thinking..."):
                answer = chat_with_ai("What is phishing and how can I recognize phishing attempts?")
                st.info(answer)
        
        if st.button("🔒 How to create strong passwords?", use_container_width=True):
            with st.spinner("🤖 Thinking..."):
                answer = chat_with_ai("What makes a strong password and how should I manage passwords?")
                st.info(answer)

# TAB 2: Security Tips
with tab2:
    st.subheader("AI-Generated Security Best Practices")
    
    st.markdown("""
    Get the latest cybersecurity recommendations and best practices 
    powered by AI. These tips are generated based on current security trends.
    """)
    
    if st.button("🎯 Generate Security Tips", type="primary", use_container_width=True):
        with st.spinner("🤖 Generating security tips... This may take 10-20 seconds..."):
            tips = generate_security_tips()
        
        st.success("✅ Tips Generated!")
        st.markdown("### 📋 Cybersecurity Best Practices")
        st.info(tips)
    
    st.divider()
    
    # Info box
    st.info("""
    **💡 How to use this assistant:**
    - Ask any cybersecurity-related question
    - Get instant AI-powered answers
    - Generate personalized security tips
    - Learn about threats and protections
    """)

# Footer
st.markdown("---")
st.caption(f"🔐 Logged in as: {st.session_state.username} | Powered by AngryPanda🐼")
