# Week 11 - Security Incident Class
# This class represents a cybersecurity incident

class SecurityIncident:
    """
    A class to represent a security incident
    Like a container for incident information
    """
    
    def __init__(self, incident_id, date, incident_type, severity, status, description, reported_by=None):
        """
        Constructor - creates a new incident object
        
        Parameters:
            incident_id (int) - unique ID number
            date (str) - when incident happened
            incident_type (str) - type of incident (like "Phishing")
            severity (str) - how serious it is (like "High")
            status (str) - current status (like "Open")
            description (str) - what happened
            reported_by (str) - who reported it (optional)
        """
        # Store all the incident data privately
        self.__id = incident_id
        self.__date = date
        self.__incident_type = incident_type
        self.__severity = severity
        self.__status = status
        self.__description = description
        self.__reported_by = reported_by
    
    def get_id(self):
        """Get the incident ID"""
        return self.__id
    
    def get_date(self):
        """Get the incident date"""
        return self.__date
    
    def get_incident_type(self):
        """Get the type of incident"""
        return self.__incident_type
    
    def get_severity(self):
        """Get how serious the incident is"""
        return self.__severity
    
    def get_status(self):
        """Get the current status"""
        return self.__status
    
    def get_description(self):
        """Get the full description"""
        return self.__description
    
    def get_reported_by(self):
        """Get who reported the incident"""
        return self.__reported_by
    
    def update_status(self, new_status):
        """
        Change the incident status
        
        Parameters:
            new_status (str) - the new status to set
        """
        self.__status = new_status
    
    def get_severity_level(self):
        """
        Get a number for severity (makes it easy to sort)
        
        Returns:
            int - 1 (low) to 4 (critical)
        """
        # Dictionary to convert text to numbers
        severity_map = {
            "low": 1,
            "medium": 2,
            "high": 3,
            "critical": 4
        }
        
        # Get the number, or 0 if not found
        return severity_map.get(self.__severity.lower(), 0)
    
    def to_dict(self):
        """
        Convert incident to dictionary (useful for DataFrames)
        
        Returns:
            dict - incident data as dictionary
        """
        return {
            'id': self.__id,
            'date': self.__date,
            'incident_type': self.__incident_type,
            'severity': self.__severity,
            'status': self.__status,
            'description': self.__description,
            'reported_by': self.__reported_by
        }
    
    def __str__(self):
        """
        Make it easy to print the incident
        
        Returns:
            str - formatted incident info
        """
        return f"Incident {self.__id} [{self.__severity.upper()}] {self.__incident_type} - {self.__status}"
