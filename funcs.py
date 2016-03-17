"""

"""
from os import path, listdir
from os.path import isdir, isfile
from string import lowercase


def drivers():
    """
    | This function returns a list of all computer drivers
    """
    return [c+':\\' for c in lowercase if path.isdir(c+':\\')]


def get_directories(path_address):
    """
    This function returns a list of all directories are into the path
    :param path_address:str
    :return list
    """
    includes = listdir(path_address)
    result = []
    for checker in includes:
        if isdir(path_address+checker):
            result += [checker]
    return result
print get_directories("C:\\")


def get_files(path_address):
    """
    This function returns a list of all files are into the path
    :param path_address:str
    :return list
    """
    includes = listdir(path_address)
    result = []
    for checker in includes:
        if isfile(path_address+checker):
            result += [checker]
    return result
