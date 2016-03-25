from __Classes import *
from PyQt4 import QtGui
from os import *
from os.path import isdir
from visual import *
from navigation import *

memory = []                                         # This list includes a number and a list
# Number is 0 for copy or 1 for cut and list has strings of file or directory names


def new_directory_action(directory_name, current_path):
    """
    | This void function creates a new directory into the current_path
    :param directory_name : str
    :param current_path:str
    """
    mkdir(current_path + directory_name)


def new_file_action(file_name, type, current_directory):
    """
    |This void function creates new file with specific name and type in current_directory
    :param file_name:str
    :param type:str
    :param current_directory
    """
    mknod(current_directory + file_name + type)


def copy_action(file_name, current_directory, memory_list=memory):
    """
    | This function saves a list of files those must copy to another directory to the memory list
    copy_action(files_names, current_directory[, memory_list=memory])
    :param file_name:str
    :param current_directory:str
    :param memory_list:list
    """
    # print '****'
    # print type(file_name)
    # print type(current_directory)
    if file_name:
        if len(memory_list):
            for element_index in range(len(memory_list)):
                memory_list.pop()
        memory_list.append(0)
        memory_list.append(current_directory + file_name)
    # print memory
    # print "______________________________________________________________________"


def cut_action(file_name, current_directory, memory_list=memory):
    # print "CUT"
    """
    | This function saves a list of files those must cut to another directory to the memory list
    copy_action(files_names, current_directory[, memory_list=memory])
    :param file_name:str
    :param current_directory:str
    :param memory_list:list
    """
    if file_name:
        if len(memory_list):
            for element_index in range(len(memory_list)):
                memory_list.pop()
        memory_list.append(1)
        memory_list.append(current_directory + file_name)


def paste_action(current_directory, list_widget, memory_list=memory):
    # print "PASTE"
    """
    | This function will paste(copy or cut) all elements are in the memory list.
    paste(current_directory[, memory_list=memory])
    :param current_directory:str
    :param list_widget:QListWidget
    :param memory_list:list
    """
    if memory_list:
        if not memory_list[0]:
            if isdir(memory_list[1]):
                directory = Directory(memory_list[1])
                directory.copy(current_directory)
            else:
                file_object = File(memory_list[1])
                file_object.copy(current_directory)
        else:
            if isdir(memory_list[1]):
                directory = Directory(memory_list[1])
                directory.cut(current_directory)
            else:
                file_object = File(memory_list[1])
                file_object.cut(current_directory)
    listView(current_directory, list_widget)


def delete_action(items, current_directory):
    """
    |This void function delet all items in current_directory.
    :param items:list
    :param current_directory:str
    """
    for item in items:
        if isdir(item):
            directory = Directory(current_directory + item)
            directory.delete()
        else:
            file_object = File(current_directory + item)
            file_object.delete()


def mEditAcUndo_triggered():
    pass

def mEditAcFind_triggered():
    pass

def mHelpAcAbout_triggered():
   msg = QtGui.QMessageBox()
   msg.setIcon(QtGui.QMessageBox.Information)
   msg.setWindowTitle("About AP file manager...")
   msg.setText('<b>This is program was developed as the first AP Project.</b>'
               '<br> Git Repository:<a href="https://github.com/mrbahrani/File-Managment-AP-Project">'
               'https://github.com/mrbahrani/File-Managment-AP-Project</a>')
   #msg.setInformativeText("This is additional information")
   #msg.setWindowTitle("MessageBox demo")
   #msg.setDetailedText("The details are as follows:")
   #msg.setStandardButtons(QtGui.QMessageBox.Ok | QtGui.QMessageBox.Cancel)
   #msg.buttonClicked.connect(msgbtn)
   msg.exec_()


def show_help_pdf():
    """
    | This void function opens help pdf file.
    """
    pdf = File('help.pdf')
    pdf.openf()


def btnFor_clicked():
    pass

def btnBack_clicked():
    pass

def btnUp_clicked():
    pass


def list_Dclicked(*args):
    """

    :param args:0.current address,1.file name(+format),2.list widget
    :return:
    """
    """
    :param args:
    :return:
    """
    # print "^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^"


    if not (args[0]):
        curDir = Directory(args[1])
        args[2].clear()
        listView(curDir.fullAddress, args[2])
        add_here(args[1])
    elif isdir(args[0] + "\\" + args[1]):
        curDir = Directory(args[0] + "\\" +args[1])
        args[2].clear()
        listView(curDir.fullAddress + "\\",args[2])
        add_here(curDir.fullAddress)
    else:
        curFile =File(args[0]+ "\\" +args[1])
        # print(curFile.fullPath,"->kir<-")
        curFile.openf()
    # print history_list




