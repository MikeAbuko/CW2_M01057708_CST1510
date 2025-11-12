import bcrypt
import os

USER_DATA_FILE = "users.txt"

def hash_password(plain_text_pass):
    """Hash a plaintext password and return the hash as a UTF-8 string."""
    pass_bytes = plain_text_pass.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed_pass = bcrypt.hashpw(pass_bytes, salt)
    return hashed_pass.decode('utf-8')

def verify_password(plain_text_password, hashed_password):
    """Verify a plaintext password against a stored hash (str or bytes)."""
    password_bytes = plain_text_password.encode('utf-8')
    if isinstance(hashed_password, str):
        hashed_password_bytes = hashed_password.encode('utf-8')
    else:
        hashed_password_bytes = hashed_password
    return bcrypt.checkpw(password_bytes, hashed_password_bytes)

def user_exists(username):
    if not os.path.exists(USER_DATA_FILE):
        return False
    with open(USER_DATA_FILE, "r", encoding="utf-8") as f:
        for line in f:
            available_user, _ = line.strip().split(',', 1)
            if available_user == username:
                return True
    return False

def register_user(username, password):
    if user_exists(username):
        print(f"Error: Username {username} already exists.")
        return False
    hashed_password = hash_password(password)
    with open(USER_DATA_FILE, "a", encoding="utf-8") as f:
        f.write(f"{username},{hashed_password}\n")
    print(f"Success: User '{username}' registered successfully!")
    return True

def login_user(username, password):
    if not os.path.exists(USER_DATA_FILE):
        print("Error: User data file not found.")
        return False
    with open(USER_DATA_FILE, "r", encoding="utf-8") as f:
        for line in f:
            user, hash_str = line.strip().split(',', 1)
            if user == username:
                if verify_password(password, hash_str):
                    print(f"Success: Welcome, {username}!")
                    return True
                else:
                    print("Error: Invalid password.")
                    return False
    print("Error: Username not found.")       
    return False

def validate_username(username):
    """Return (is_valid: bool, error_message: str)."""
    if len(username) < 3 or len(username) > 20:
        return False, "Username must be between 3 and 20 characters."
    if not username.isalnum():
        return False, "Username cannot contain special characters."
    return True, ""

def validate_password(password):
    """Return (is_valid: bool, error_message: str)."""
    if len(password) < 6:
        return False, "Password must be at least 6 characters long."
    if not any(char.isdigit() for char in password):
        return False, "Password must contain at least one digit."
    if not any(char.isupper() for char in password):
        return False, "Password must contain at least one uppercase letter."
    if not any(char.islower() for char in password):
        return False, "Password must contain at least one lowercase letter."
    return True, ""

def display_menu():
    print("\n" + "="*50)
    print("  MULTI-DOMAIN INTELLIGENCE PLATFORM")
    print("  Secure Authentication System")
    print("="*50)
    print("\n[1] Register a new user")
    print("[2] Login")
    print("[3] Exit")
    print("-"*50)

def main():
    print("\nWelcome to the Week 7 Authentication System!")

    while True:
        display_menu()
        choice = input("\nPlease select an option (1-3): ").strip()

        if choice == '1':
            # Registration flow
            print("\n--- USER REGISTRATION ---")
            username = input("Enter a username: ").strip()

            # Username validation
            is_valid, error_msg = validate_username(username)
            if not is_valid:
                print(f"Error: {error_msg}")
                continue

            password = input("Enter a password: ").strip()

            # Password validation
            is_valid, error_msg = validate_password(password)
            if not is_valid:
                print(f"Error: {error_msg}")
                continue

            # Password comparison
            password_confirm = input("Confirm password: ").strip()
            if password != password_confirm:
                print("Error: Passwords do not match.")
                continue

            # Register new user
            register_user(username, password)

        elif choice == '2':
            # Entering login credentials
            print("\n--- USER LOGIN ---")
            username = input("Enter your username: ").strip()
            password = input("Enter your password: ").strip()

            # Attempt login
            if login_user(username, password):
                print("\nYou are now logged in.")
                print("(In a real application, you would now access the dashboard or protected resources.)")
                # Asking user if they want to logout or exit
                input("\nPress Enter to return to main menu...")

        elif choice == '3':
            # Exiting the program
            print("\nThank you for using the authentication system.")
            print("Exiting...")
            break

        else:
            print("\nError: Invalid option. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()