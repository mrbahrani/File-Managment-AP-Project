from __Classes import *
from PyQt4 import QtGui
from os import mknod, mkdir

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
    for element in memory_list:
        memory_list.pop()
    for element_index in range(len(files_names)):
        files_names[element_index] = current_directory + files_names[element_index]
    memory_list += [0, files_names]


def mEditAcCut_triggered():
    pass

def mEditAcPaste_triggered():
    pass

def mEditAcDelete_triggered():
    pass

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
def mHelpAcHelp_triggered():
    pass


def btnFor_clicked():
    pass

def btnBack_clicked():
    pass

def btnUp_clicked():
    pass


