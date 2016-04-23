import socket
from events import *
from search import search
from os.path import isdir, isfile
from os import listdir
from db import  get_setting_value
def clientListView(final_string,listView):
    initList = final_string.split("|")
    fileList = []
    dirList = []
    for item in initList:
        if item[1]:
            fileList += [item[1:]]
        else:
            dirList += [item[1:]]
    for dirItem in dirList:
        new =QtGui.QListWidgetItem(listView)
        new.setText(dirItem)
        icon = QtGui.QIcon('icons/folder.ico')
        new.setIcon(icon)
    for fileItem in fileList:
        new = QtGui.QListWidgetItem(listView)
        new.setText(dirItem)
        icon =QtGui.QIcon(file_icon(fileItem))
        new.setIcon(icon)