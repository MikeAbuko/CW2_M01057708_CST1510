# Week 7: Secure Authentication System

Student Name: Mike Abuko  
Student ID: M01057708 
Course: CST1510 -CW2 -  Multi-Domain Intelligence Platform 

## Project Description

A command-line authentication system implementing secure password hashing
This system allows users to register accounts and log in with proper pass

## Features
- Secure password hashing using bcrypt with automatic salt generation
- User registration with duplicate username prevention
- User login with password verification
- Input validation for usernames and passwords
- File-based user data persistence
- Password confirmations during login and registration
- Error messages to inform the user what is wrong

## Technical Implementation
- Hashing Algorithm: bcrypt with automatic salting
- Data Storage: Plain text file (`users.txt`) with comma-separated values
- Password Security: One-way hashing, no plaintext storage
- Validation: Username (3-20 alphanumeric characters), Password (6-50 characters) - Must contain atleast: one digit, uppercase, and lowercase letters.


## Project Progress

### Week 7: User Authentication (Completed)
- Created a user registration and login system
- Used bcrypt to hash passwords for security
- Stored the users in a text file (users.txt)
- Made sure usernames and passwords follow the rules

### Week 8: Database Integration (Completed)
**What I did:**
- Set up SQLite database to store all the data
- Created 4 tables:
  - `users` - stores user accounts
  - `cyber_incidents` - stores security incidents
  - `datasets_metadata` - stores dataset information
  - `it_tickets` - stores IT support tickets

- Moved my login/register functions to work with the database instead of users.txt file making it more dynamic
- Learned CRUD (Create, Read, Update, Delete)
- Made sure to use `?` placeholders to prevent SQL injection attacks
- Tested to make sure it works

**Files created:**
- `app/data/db.py` - connects to the database
- `app/data/schema.py` - creates the tables
- `app/data/users.py` - handles user operations
- `app/data/incidents.py` - handles incidents
- `app/data/datasets.py` - handles datasets
- `app/data/tickets.py` - handles tickets
- `app/services/user_service.py` - handles user login/registration with database
- `main.py` - demo script to test that the backend functionality works well.

## How to Run

1. Install the required packages:

- pip install -r requirements.txt


2. Run the demo:
- python main.py

This will:
- Create the database file
- Set up all the tables
- Test user registration and login
- Show how CRUD operations work

## Requirements

- Python
- bcrypt - for security
- pandas - for working with data

### Week 9: Web Interface (Completed)
**What I did:**
- Built a complete web application using Streamlit
- Created 5 pages:
  - `Home.py` - Login and registration
  - `1_Dashboard.py` - Main page with quick stats
  - `2_Incidents.py` - View, add, edit, delete cyber incidents
  - `3_Datasets.py` - View, add, edit, delete datasets
  - `4_Tickets.py` - View, add, edit, delete IT tickets
  - `5_Analytics.py` - Charts and visualizations

- Added session state to keep users logged in
- Protected all pages so only logged-in users can access them
- Made CRUD forms for all data types
- Added data visualization with charts
- Made it look professional with custom styling

**Files created:**
- `Home.py` - Main login page
- `pages/Dashboard.py` through `pages/Analytics.py` - All app pages

### Week 10: AI Integration (Completed)
**What I learned:**
- How to use external AI APIs in my application
- Working with Hugging Face Inference API
- Storing API keys securely using Streamlit secrets
- Creating AI-powered features for cybersecurity analysis
- Writing prompts to get good responses from AI

**What I built:**
- **AI Service Module** (`app/services/ai_service.py`)
  - `analyze_security_incident()` - AI analyzes incidents
  - `generate_security_tips()` - AI creates security tips
  - `chat_with_ai()` - Chat with AI about security

- **AI Assistant Page** (`pages/AI_Assistant.py`)
  - Ask AI any cybersecurity question
  - Quick question buttons for common topics
  - Generate security best practices
  - Get instant AI-powered answers

- **Enhanced Incidents Page**
  - AI-powered incident analysis button
  - Threat level assessment from AI
  - Automatic recommendations

**Technologies used:**
- **Hugging Face Inference API** - Access to AI models
- **Mistral-7B-Instruct-v0.2** - The AI model we use
- **Streamlit Secrets** - Secure way to store API keys
- **huggingface_hub** Python library

**Features:**
✅ AI analyzes security incidents  
✅ Chat with AI about cybersecurity  
✅ Generate security tips automatically  
✅ Get threat assessments  
✅ Quick questions with preset answers  
✅ Secure API key storage  

**New files:**
- `.streamlit/secrets.toml` - Stores API key (not uploaded to git)
- `app/services/ai_service.py` - AI integration functions
- `pages/AI_Assistant.py` - AI chat page
- `test_ai.py` - Test script

**Modified files:**
- `pages/Incidents.py` - Added AI analysis
- `pages/Dashboard.py` - Added AI features section
- `requirements.txt` - Added huggingface_hub

**How to use:**
1. Go to **Incidents** page
2. Add or select an incident
3. Click "Analyze with AI" to get assessment
4. Visit **AI Assistant** page to chat
5. Ask questions or generate tips

**Setting up API key:**
1. Make account at https://huggingface.co
2. Go to Settings → Access Tokens
3. Create new token with "Read" access
4. Put it in `.streamlit/secrets.toml`:
   ```toml
   HF_TOKEN = "your_token_here"
   ```
5. Never upload secrets.toml to GitHub (it's in .gitignore)
