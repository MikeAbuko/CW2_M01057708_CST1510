# Week 11 - User Class
# This class is for a user in our system

class User:
    """
    A class to represent a user
    This is like a template for creating user objects
    """
    
    def __init__(self, username, password_hash, role):
        """
        Constructor - runs when we create a new User object
        
        Parameters:
            username (str) - the user's name
            password_hash (str) - encrypted password
            role (str) - user's role (like "admin" or "user")
        """
        # Private attributes (use double underscore)
        self.__username = username
        self.__password_hash = password_hash
        self.__role = role
    
    def get_username(self):
        """
        Get the username
        
        Returns:
            str - the username
        """
        return self.__username
    
    def get_password_hash(self):
        """
        Get the password hash
        
        Returns:
            str - the hashed password
        """
        return self.__password_hash
    
    def get_role(self):
        """
        Get the user's role
        
        Returns:
            str - the role
        """
        return self.__role
    
    def verify_password(self, plain_password, password_verifier):
        """
        Check if a plain-text password matches this user's hash
        
        Parameters:
            plain_password (str) - password to check
            password_verifier (function) - function that verifies password
            
        Returns:
            bool - True if password matches, False otherwise
        """
        return password_verifier(plain_password, self.__password_hash)
    
    def __str__(self):
        """
        String representation - makes it easy to print the user
        
        Returns:
            str - formatted user info
        """
        return f"User({self.__username}, role={self.__role})"
