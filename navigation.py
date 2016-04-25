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
history_list = []                           # History container
winList = []
here = []                                    # The index of current directory


def add_here(directory_path, window_index, h_list=history_list, here_index=here, parent=None):
    """
    |This void function adds current directory to the history list in a very confusing way!
    add_here(directory_path[, h_list=history_list])
    :param directory_path:str
    :param h_list:list
    :param here_index:list
    """
    directory = Directory(directory_path)
    print 'KIR'
    print directory_path
    # try:
    # print h_list
    index = here_index[window_index][0]
    if parent is None:
        for element_index in range(len(h_list[window_index]) - 1, 0, -1):
            if h_list[window_index][element_index][1] == directory.parent:
                # print "---------------------------------"
                # print h_list[element_index][1]
                # print directory.parent
                # print "^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^"
                for element in range(len(h_list[window_index]) - 1, element_index - 1, -1):
                    h_list[window_index].pop()
                here_index[window_index].pop()
                h_list[window_index].append([directory_path.replace('\\\\', '\\'), directory.parent])
                here_index[window_index].append(len(h_list[window_index]) - 1)
                return
        h_list[window_index].append([directory_path.replace('\\\\', '\\'), directory.parent])
    else:
        h_list[window_index].append([directory_path.replace('\\\\', '\\'), "*"])
    here_index[window_index].pop()
    here_index[window_index].append(index + 1)

    # except Exception as e:
    #     print 'here exception'


def history_back(ui, window_index, index=here, history=history_list):
    """
    |This function returns a step back from current index of history as a list
    history_back([index=here])
    :param list_widget:QListWidget
    :param index:int
    :param history:list
    """
    try:
        if index[0] and history[window_index][index[window_index][0] - 1] != "*\\*":
            index_num = index[window_index][0] - 1
            index[window_index].pop()
            index[window_index].append(index_num)
            ui.listView.clear()
            if history[window_index][index_num][0]:
                listView(history[window_index][index_num][0] + "\\", ui.listView)
                ui.lineEdit.setText(history[window_index][index_num][0] + "\\")
            else:
                listView("", ui.listView)
                ui.lineEdit.setText("")
    except IndexError:
        return 'index error'


def history_forward(ui, window_index, index=here, history=history_list):
    """
    |This function returns a step forward from current index of history as a list
    history_forward([index=here])
    :param list_widget:QListWidget
    :param index:int
    :param history:list
    """
    try:
        if index[window_index][0] < len(history[window_index]) - 1 and history[window_index][index[window_index][0] + 1] != "*\\*":
            index_num = index[window_index][0] + 1
            index[window_index].pop()
            index[window_index].append(index_num)
            ui.listView.clear()
            if history[window_index][index[window_index][0]][0]:
                listView(history[window_index][index[window_index][0]][0] + "\\", ui.listView)
                ui.lineEdit.setText(history[window_index][index[window_index][0]][0] + "\\")
            else:
                listView("", ui.listView)
                ui.lineEdit.setText("")
    except IndexError:
        return False
