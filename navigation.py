"""
This file included files and variables needed for user file navigation.
List of variables:
1.history_list : list
2.here : int
List of functions:
1.add_here
2.history_back
3.history_forward
4.index_distance
"""
from __Classes import Directory
history_list = [["", ""]]                           # History container
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
        h_list += [[(directory_path + "\\").replace("\\\\", "\\"), directory.parent + ""]]
        here = len(history_list) - 1



def history_back(index=here, history=history_list):
    """
    |This function returns a step back from current index of history as a list
    history_back([index=here])
    :param index:int
    :param history:list
    """
    try:
        index -= 1
        return history[index]
    except IndexError:
        return False


def history_forward(index=here, history=history_list):
    """
    |This function returns a step forward from current index of history as a list
    history_forward([index=here])
    :param index:int
    :param history:list
    """
    try:
        index += 1
        return history[index]
    except IndexError:
        return False


def index_distance(index=here, history=history_list):
    """
    | This function returns the distance between current directory and end of the history list.
    | If it return 0, There is no forward directory
    | And if it return the length of history_list, there is no backward directory
    index_distance([index=here][, history=history_list])
    :param index:int
    :param history:list
    """
    return len(history) - index
