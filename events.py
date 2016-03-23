from __Classes import *
from PyQt4 import QtGui
from os import *
from os.path import isdir
from visual import *

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

def copy_action(files_names, current_directory, memory_list=memory):
    """
    | This function saves a list of files those must copy to another directory to the memory list
    copy_action(files_names, current_directory[, memory_list=memory])
    :param files_names:list
    :param current_directory:str
    :param memory_list:list
    """
    if type(files_names) != list:
        files_names = list(files_names)
    if "" in files_names:
        return
    for element in range(len(memory_list)):
        memory_list.pop()
    for element_index in range(len(files_names)):
        files_names[element_index] = current_directory + files_names[element_index]
    memory_list += [0, files_names]


def cut_action(files_names, current_directory, memory_list=memory):
    """
    | This function saves a list of files those must cut to another directory to the memory list
    copy_action(files_names, current_directory[, memory_list=memory])
    :param files_names:list
    :param current_directory:str
    :param memory_list:list
    """
    for element in memory_list:
        memory_list.pop()
    for element_index in range(len(files_names)):
        files_names[element_index] = current_directory + files_names[element_index]
    memory_list += [1, files_names]


def paste_action(current_directory, memory_list=memory):
    """
    | This function will paste(copy or cut) all elements are in the memory list.
    paste(current_directory[, memory_list=memory])
    :param current_directory:str
    :param memory_list:list
    """
    if not memory_list[0]:
        for element in memory_list[1]:
            print '$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$4'
            print element
            print isdir(element)
            if isdir(element):
                directory = Directory(element)
                directory.copy(current_directory + directory.name)
            else:
                file_object = File(element)
                file_object.copy(current_directory)
    else:
        for element in memory_list[1]:
            if isdir(element):
                directory = Directory(element)
                directory.cut(current_directory)
            else:
                file_object = File(element)
                file_object.cut(current_directory)


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
    print args
    if isdir(args[0]+ "\\" + args[1]):
        curDir = Directory(args[0] + "\\" +args[1])
        args[2].clear()
        listView(curDir.fullAddress,args[2])
    else:
        curFile =File(args[0]+ "\\" +args[1])
        curFile.openf()





