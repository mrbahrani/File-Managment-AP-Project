import socket
from events import *
from search import search
from os.path import isdir, isfile
from os import listdir
from db import  get_setting_value
from Client import *

def sock_drivers():
    file_list_request(get_setting_value("username"),,""):

def clientListView(final_string,listView):
    '''
    initList = final_string.split("|")
    fileList = []
    dirList = []
    for item in initList:
        if item[1]:
            fileList += [item[1:]]
        else:
            dirList += [item[1:]]
    '''
    dirfile_list = dir_file_list(final_string)
    dirList = dirfile_list[0]
    fileList = dirfile_list[1]

    for dirItem in dirList:
        new =QtGui.QListWidgetItem(listView)
        new.setText(dirItem)
        icon = QtGui.QIcon('..\\icons/folder.ico')
        new.setIcon(icon)

    for fileItem in fileList:
        new = QtGui.QListWidgetItem(listView)
        new.setText(fileItem)
        icon = QtGui.QIcon(file_icon(fileItem))
        new.setIcon(icon)
    #result = []
    #result.append(dirList)
    #result.append(fileList)
    #return result

def dir_file_list(final_string) :
    initList = final_string.split("|")
    fileList = []
    dirList = []
    for item in initList:
        if item[1]:
            fileList += [item[1:]]
        else:
            dirList += [item[1:]]
    result = []
    result.append(dirList)
    result.append(fileList)
    return result
def sock_list_Dclicked(*args):
    """
    :param args:0.current address,1.file name(+format),2.list widget
    :return:
    :param args:
    :return:
    """
    lLock[args[4]].acquire()
    if not (args[0]):
        curDir = Directory(args[1])
        args[2].clear()
        # print curDir.fullAddress
        print curDir.fullAddress
        listView(curDir.fullAddress, args[2])
        add_here(args[1], args[4])
        args[3].setText(args[1])
    elif args[0] == "*\\*":
        args[2].clear()
        listView(args[1], args[2])
        add_here(args[1], args[4])
        args[3].setText(args[1])

    elif isdir(args[0] + "\\" + args[1]):
        print args[0] + "\\" + args[1],"this"
        curDir = Directory(args[0] + "\\" +args[1])
        args[2].clear()
        #print curDir.fullAddress
        listView(curDir.fullAddress + "\\", args[2])
        add_here(curDir.fullAddress, args[4])
        args[3].setText(curDir.fullAddress)
    else:
        print args[0] + "\\" +args[1],"that"
        curFile =File(args[0] + "\\" +args[1])
        print curFile.fullPath,
        curFile.openf()
    lLock[args[4]].release()
    # print "***********"
    # print history_list
    # print "XXXXXXXXXXXXXXXXXXXXXXXXX"
