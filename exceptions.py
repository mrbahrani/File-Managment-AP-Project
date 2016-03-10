"""
This file including exception classes.
Exceptions list:
1.FileNotExist
"""


class FileNotExist(Exception):
    def __init__(self):
        super(FileNotExist).__init__(self)

    def __str__(self):
        return "File not exist"
