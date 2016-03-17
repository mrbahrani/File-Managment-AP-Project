from __Classes import *
from DefaultUI import *
from PyQt4 import QtGui
from funcs import *


def file_icon(file_name):
    """
    | This function returns proper icon path for file type
    :param file_name:str
    :return str
    """
    file_type = file_name.split('.')[-1]
    icons_types = [['mkv', 'mp4', 'avi', 'icon/movie.ico'], ['mp3', 'flac', 'wav', 'icons/music.ico']]
    icons_types += [['docx, doc', 'icons/word.ico'], ['jpg', 'jpeg', 'gif', 'ttf', 'ico', 'png', 'icons/picture.ico']]
    icons_types += ['zip', 'rar', 'gzip', 'icons/zip.ico']
    for checker in icons_types:
        if file_type in checker:
            return checker[-1]
        else:
            return 'icons/text.ico'


def treeView(fullPath,qwtIt):
    #This function visualizes the tree view of the directories
    try:
        dirList= get_directories(fullPath)
        if bool(dirList):
            for it in dirList:
                i = QtGui.QTreeWidgetItem()
                i.setText(0,it)
                qwtIt.addChild(i)

    except WindowsError:
        print("Accsess denied")
    except Exception:
        print("An unwanted exception occurred!!")


def listView(full_path, list_view):
    """
    This function visualizes the list view of the directories
    :param full_path:str
    :param list_view:obj
    """
    try:
        dir_list = get_directories(full_path)
        files_list = get_files(full_path)
        if dir_list:
            for it in dir_list:
                print 'kir'
                item = QtGui.QListWidgetItem(list_view)
                item.setText(it)
                icon = QtGui.QIcon('icons/folder.ico')
                item.setIcon(icon)

        if files_list:
            for file_name in files_list:
                item = QtGui.QListWidget(list_view)
                item.setText(file_name)
                icon = QtGui.QIcon(file_icon(file_name))
                item.setIcon(icon)

    except WindowsError:
        print("Access denied")
    except:
        print("An unwanted exception ocurred!!")