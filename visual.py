from __Classes import *
from DefaultUI import *
from PyQt4 import QtGui
from funcs import *
from os.path import isdir
from funcs import remove_equals
from threading import Lock
lLock = Lock()
def file_icon(file_name):
    """
    | This function returns proper icon path for file type
    :param file_name:str
    :return str
    """
    file_type = file_name.split('.')[-1].lower()
    # print file_type
    icons_types = [['mkv', 'mp4', 'avi', 'f4v', 'flv', 'icons/movie.ico'], ['mp3', 'flac', 'wav', 'icons/music.ico']]
    icons_types += [['docx, doc', 'icons/word.ico'], ['jpg', 'jpeg', 'gif', 'ttf', 'ico', 'png', 'icons/picture.ico']]
    icons_types += ['zip', 'rar', 'gzip', 'icons/zip.ico']
    for checker in icons_types:
        if file_type in checker:
            return checker[-1]
    return 'icons/text.ico'


def treeView(fullPath,qwtIt):
    #This function visualizes the tree view of the directories
    lLock.acquire()
    try:
        if not qwtIt.isUsed:
            dirList= get_directories(fullPath)
            if bool(dirList):
                for it in dirList:
                    icon = QtGui.QIcon('icons/folder.ico')
                    i = QtGui.QTreeWidgetItem()
                    i.setText(0,it)
                    i.setIcon(0,icon)
                    i.dir = fullPath+it+"\\"
                    i.isUsed = False
                    qwtIt.addChild(i)

    except WindowsError:
        print("Accsess denied")
    except Exception, e:
        print("An unwanted exception occurred!!")
        print e
    qwtIt.isUsed = True
    lLock.release()

def listView(full_path, list_view):
    """
    This function visualizes the list view of the directories
    :param full_path:str
    :param list_view:obj
    """
    lLock.acquire()
    try:
        # print "KIR"
        # print full_path
        if full_path == "":
            # print 1
            dir_list = drivers()
            files_list = []
        elif type(full_path) == list and not full_path:
            # print 2
            dir_list = full_path
            files_list = get_files("")
        elif type(full_path) == list and type(full_path[0]) == list:
            # print 3
            dir_list, files_list = [], []
            for element in full_path:
                if isdir(element[0]):
                    dir_list += [element[0]]
                else:
                    files_list += [element[0]]
            dir_list = remove_equals(dir_list)
            files_list = remove_equals(files_list)
        elif type(full_path) == list:
            dir_list, files_list = [], []
            for element in full_path:
                if isdir(element):
                    dir_list.append(element)
                else:
                    files_list.append(element)
        else:
            # print 4
            dir_list = get_directories(full_path)
            files_list = get_files(full_path)
        # print "*****"
        # print dir_list
        if dir_list:
            for it in dir_list:
                item = QtGui.QListWidgetItem(list_view)
                item.setText(it)
                icon = QtGui.QIcon('icons/folder.ico')
                item.setIcon(icon)

        if files_list:
            for file_name in files_list:
                item = QtGui.QListWidgetItem(list_view)
                item.setText(file_name)
                icon = QtGui.QIcon(file_icon(file_name))
                item.setIcon(icon)

    except WindowsError:
        print("Access denied")
    lLock.release()
    # except Exception as e:
    #     print("An unwanted exception ocurred!!")
    #     print e
