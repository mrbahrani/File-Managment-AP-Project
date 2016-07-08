import socket
from events import *
from search import search
from os.path import isdir, isfile
from os import listdir
from db import  get_setting_value
from Client import *
#from __Classes import *

#this two lists keeping last request of file and dir list from server
last_request_directory_list = []
last_request_files_list = []

provider_username_list = []

#directory which we are in right now (for each window) (directory [0] is for first window) (something like history list last element)
directory = [""]


def get_sock_drivers():
    if not provider_username_list:
        return
    file_list_request(get_setting_value("user_name"), provider_username_list[0],"")



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


def dir_file_list(request_string, files_list=last_request_files_list, dir_list=last_request_directory_list):
    """
    | This function gets request_string and then appends all directories to last_request_directory_list and all files to
    | last_request_files_list.
    | Attention: Do not fill files_list and dir_list parameters.
    :param request_string: str
    :param files_list: list
    :param dir_list: list
    :return void
    """
    request_list = request_string.split("|")[3:]
    for item in request_list:
        if not item:
            continue
        if item[0] == "0":
            dir_list.append(item[1:])
        elif item[0] == "1":
            files_list.append(item[1:])
    print "Vasat daram"
    print last_request_directory_list
    print last_request_files_list

def sock_list_Dclicked(*args):
    """
    :param args:0.current address,1.file name(+format),2.list widget,3.line edit,4.window index
    :return:
    :param args:
    :return:
    """
    # lLock[args[4]].acquire()
    if not (args[0]):
        curDir = Directory(args[1])
        args[2].clear()
        # print curDir.fullAddress
        print curDir.fullAddress
        clientListView(curDir.fullAddress, args[2])
        #add_here(args[1], args[4])
        directory[args[4]] += (args[1])
        args[3].setText(args[1])
    elif args[0] == "*\\*":
        args[2].clear()
        clientListView(args[1], args[2])
        #add_here(args[1], args[4])
        directory[args[4]] += (args[1])
        args[3].setText(args[1])

    elif isdir(args[0] + "\\" + args[1]):
        print args[0] + "\\" + args[1],"this"
        curDir = Directory(args[0] + "\\" +args[1])
        args[2].clear()
        #print curDir.fullAddress
        clientListView(curDir.fullAddress + "\\", args[2])
        #add_here(curDir.fullAddress, args[4])
        directory[args[4]] += ('\\'+args[1])
        args[3].setText(curDir.fullAddress)
    else:
        print args[0] + "\\" +args[1],"that"
        curFile =File(args[0] + "\\" +args[1])
        print curFile.fullPath,
        curFile.openf()
    # lLock[args[4]].release()
    # print "***********"
    # print history_list
    # print "XXXXXXXXXXXXXXXXXXXXXXXXX"

def sock_treeView(fullPath,qwtIt):
    #This function visualizes the tree view of the directories
    try:
        if not qwtIt.isUsed:
            dirList= dir_file_list(fullPath)[0]
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
