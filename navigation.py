"""
This file included files and variables needed for user file navigation.
List of variables:

List of functions
"""
from __Classes import Directory
history_list = []                           # History container
here = 0                                    # The index of current directory


def add_here(directory_path, h_list=history_list):
    """
    |This void function adds current directory to the history list in a very confusing way!
    add_here(directory_path[, h_list=history_list])
    :param directory_path:str
    :param h_list:list
    """
    directory = Directory(directory_path)
    try:
        parent_lindex =[h_list.index(x) for x in h_list if x[1] == directory.parent][-1]
        if h_list[parent_lindex][0] != directory_path:
            for remover in range(parent_lindex, len(h_list)):
                h_list.pop(remover + 1)
    except IndexError:
        pass
    finally:
        h_list.append([directory_path, directory.parent])


# while 1:
#     add_here(str(raw_input(':')))
#     print history_list
