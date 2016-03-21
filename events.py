from __Classes import *
from DefaultUI import *
from PyQt4 import QtGui
from funcs import *
from os import *


def new_directory_action(directory_name, current_path):
    """
    | This function creates a new directory into the current_path
    :param directory_name : str
    :param current_path:str
    """
    mkdir(current_path + directory_name)

def mFileAcNFile(filename,type,currentDirectory):
    pass

def mEditAcCopy_triggered():
    pass

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


