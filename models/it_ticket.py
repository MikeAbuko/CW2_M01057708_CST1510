# Week 11 - IT Ticket Class
# This class is for an IT support ticket

class ITTicket:
    """
    A class to represent an IT ticket
    Like a help desk request
    """
    
    def __init__(self, ticket_id, title, priority, status, category=None, assigned_to=None, created_date=None):
        """
        Constructor - creates a new ticket object
        
        Parameters:
            ticket_id (int) - unique ticket number
            title (str) - ticket title
            priority (str) - how urgent (like "High")
            status (str) - current status (like "Open")
            category (str) - ticket category (like "Hardware")
            assigned_to (str) - who is working on it
            created_date (str) - when ticket was created
        """
        self.__id = ticket_id
        self.__title = title
        self.__priority = priority
        self.__status = status
        self.__category = category
        self.__assigned_to = assigned_to if assigned_to else "Unassigned"
        self.__created_date = created_date
    
    def get_id(self):
        """Get ticket ID"""
        return self.__id
    
    def get_title(self):
        """Get ticket title"""
        return self.__title
    
    def get_priority(self):
        """Get priority level"""
        return self.__priority
    
    def get_status(self):
        """Get current status"""
        return self.__status
    
    def get_category(self):
        """Get ticket category"""
        return self.__category
    
    def get_assigned_to(self):
        """Get who it's assigned to"""
        return self.__assigned_to
    
    def get_created_date(self):
        """Get when ticket was created"""
        return self.__created_date
    
    def assign_to(self, staff):
        """
        Assign ticket to someone
        
        Parameters:
            staff (str) - staff member name
        """
        self.__assigned_to = staff
    
    def close_ticket(self):
        """Mark the ticket as closed"""
        self.__status = "Closed"
    
    def update_status(self, new_status):
        """
        Update ticket status
        
        Parameters:
            new_status (str) - new status to set
        """
        self.__status = new_status
    
    def get_priority_level(self):
        """
        Get a number for priority (makes it easy to sort)
        
        Returns:
            int - 1 (low) to 3 (high)
        """
        priority_map = {
            "low": 1,
            "medium": 2,
            "high": 3
        }
        return priority_map.get(self.__priority.lower(), 0)
    
    def to_dict(self):
        """
        Convert ticket to dictionary
        
        Returns:
            dict - ticket data as dictionary
        """
        return {
            'id': self.__id,
            'title': self.__title,
            'priority': self.__priority,
            'status': self.__status,
            'category': self.__category,
            'assigned_to': self.__assigned_to,
            'created_date': self.__created_date
        }
    
    def __str__(self):
        """
        Make it easy to print the ticket
        
        Returns:
            str - formatted ticket info
        """
        return f"Ticket {self.__id}: {self.__title} [{self.__priority}] - {self.__status} (assigned to: {self.__assigned_to})"
