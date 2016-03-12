"""
This file including exception classes.
Exceptions list:
1.FileNotExist
"""


class FileNotExist(Exception):
    """
    | This error rise When file has not exist.This class Inherit from Exception class.
    | The __str__ method of The Exception class has been overridden.
    """
    def __init__(self):
        self.massage = "File not exist"
        super(FileNotExist, self).__init__(self.massage)

    def __str__(self):
        """
        :return "File not exist" : str
        """
        return self.massage


class NoPermission(Exception):
    """
    | This error rise When the file is not readable.This class Inherit from Exception class.
    | The __str__ method of The Exception class has been overridden.
    """
    def __init__(self):
        super(NoPermission, self).__init__()

    def __str__(self):
        """
        :return "You have not right permission to change this file" : str
        """
        return "You have not right permission to change this file"
