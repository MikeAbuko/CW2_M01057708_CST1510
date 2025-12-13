# Week 11 - Dataset Class
# This class represents a data science dataset

class Dataset:
    """
    A class to represent a dataset
    Stores information about data files
    """
    
    def __init__(self, dataset_id, name, size_bytes, rows, source, format_type=None):
        """
        Constructor - creates a new dataset object
        
        Parameters:
            dataset_id (int) - unique ID
            name (str) - dataset name
            size_bytes (int) - file size in bytes
            rows (int) - number of rows
            source (str) - where it came from
            format_type (str) - file format (like "CSV", "JSON")
        """
        self.__id = dataset_id
        self.__name = name
        self.__size_bytes = size_bytes
        self.__rows = rows
        self.__source = source
        self.__format_type = format_type
    
    def get_id(self):
        """Get the dataset ID"""
        return self.__id
    
    def get_name(self):
        """Get the dataset name"""
        return self.__name
    
    def get_rows(self):
        """Get number of rows"""
        return self.__rows
    
    def get_size_bytes(self):
        """Get size in bytes"""
        return self.__size_bytes
    
    def calculate_size_mb(self):
        """
        Convert bytes to megabytes
        
        Returns:
            float - size in MB
        """
        # 1 MB = 1024 * 1024 bytes
        return self.__size_bytes / (1024 * 1024)
    
    def calculate_size_kb(self):
        """
        Convert bytes to kilobytes
        
        Returns:
            float - size in KB
        """
        return self.__size_bytes / 1024
    
    def get_source(self):
        """Get where the dataset came from"""
        return self.__source
    
    def get_format(self):
        """Get the file format"""
        return self.__format_type
    
    def to_dict(self):
        """
        Convert dataset to dictionary
        
        Returns:
            dict - dataset data as dictionary
        """
        return {
            'id': self.__id,
            'name': self.__name,
            'size_bytes': self.__size_bytes,
            'rows': self.__rows,
            'source': self.__source,
            'format': self.__format_type
        }
    
    def __str__(self):
        """
        Make it easy to print the dataset
        
        Returns:
            str - formatted dataset info
        """
        size_mb = self.calculate_size_mb()
        return f"Dataset {self.__id}: {self.__name} ({size_mb:.2f} MB, {self.__rows} rows)"
