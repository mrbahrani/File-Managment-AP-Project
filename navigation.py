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
from visual import listView
history_list = [["", ""]]                           # History container
here = [0]                                    # The index of current directory


def add_here(directory_path, h_list=history_list, here_index=here, parent=None):
    """
    |This void function adds current directory to the history list in a very confusing way!
    add_here(directory_path[, h_list=history_list])
    :param directory_path:str
    :param h_list:list
    :param here_index:list
    """
    directory = Directory(directory_path)
    try:
        # print h_list
        index = here_index[0]
        for element_index in range(len(h_list) - 1, 0, -1):
            if h_list[element_index][1] == directory.parent:
                # print "---------------------------------"
                # print h_list[element_index][1]
                # print directory.parent
                # print "^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^"
                for element in range(len(h_list) - 1, element_index - 1, -1):
                    h_list.pop()
                here_index.pop()
                h_list.append([directory_path.replace('\\\\', '\\'), directory.parent])
                here_index.append(len(h_list) - 1)
                return
        if parent is None:
            h_list.append([directory_path.replace('\\\\', '\\'), directory.parent])
        else:
            h_list.append([directory_path.replace('\\\\', '\\'), "*"])
        here_index.pop()
        here_index.append(index + 1)

    except Exception as e:
        print e


def history_back(list_widget, index=here, history=history_list):
    """
    |This function returns a step back from current index of history as a list
    history_back([index=here])
    :param list_widget:QListWidget
    :param index:int
    :param history:list
    """
    try:
        if index[0]:
            index_num = index[0] - 1
            index.pop()
            index.append(index_num)
            list_widget.clear()
            print ">>>>>>>>>>>>>>>>>>>>>>>>>> BACK <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<"
            print here
            print history
            if history[index_num][0]:
                listView((history[index_num][0] + "\\").replace("\\", "\\\\"), list_widget)
            else:
                listView("", list_widget)
    except IndexError:
        return 'index error'


def history_forward(list_widget, index=here, history=history_list):
    """
    |This function returns a step forward from current index of history as a list
    history_forward([index=here])
    :param list_widget:QListWidget
    :param index:int
    :param history:list
    """
    try:
        if index[0] < len(history) - 1:
            index_num = index[0] + 1
            index.pop()
            index.append(index_num)
            list_widget.clear()
            print ">>>>>>>>>>>>>>>>>>>>>>>>>> FORWARD <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<"
            print here
            print history
            if history[index[0]][0]:
                listView((history[index[0]][0] + "\\").replace("\\", "\\\\"), list_widget)
            else:
                listView("", list_widget)
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
    return len(history) - index[0]
