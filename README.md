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