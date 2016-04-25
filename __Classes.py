from os import rename, access, remove, R_OK, F_OK, startfile, listdir , mkdir
from os.path import isdir
from __ErrorHandler import error_show
from __exceptions import FileNotExist,NoPermission
from shutil import rmtree, copy2, copytree
from PyQt4 import QtCore, QtGui
# from Socket.Client import *
import sys


class File(object):
    def __init__(self, strAdrs):
        self.fullPath = strAdrs
        # print "******************************************"
        # print self.fullPath
        self.__existence()
        self.__reachable()
        self.type = strAdrs.split(".")[-1]
        self.name = strAdrs.split("\\")[-1][:]
        self.Jname = strAdrs.split(".")[0]
        if len(strAdrs.split("\\")) > 1:
          self.parent = strAdrs.split("\\")[-2]

    def __existence(self):
        """
        | If the file has not exist , This private method raise a FileNotExist exception
        :param self : Object
        """
        if not access(self.fullPath, F_OK):
            raise FileNotExist

    def __reachable(self):
        if not access(self.fullPath, R_OK):
            raise NoPermission

    def openf(self):
        """
        This method opens the file.
        """
        try:
            startfile(self.fullPath)
        except Exception:
            print ("An exception ocurred")

    def copy(self, dest):
        """
        This method creates a copy of the file.
        parameters:
        self : Object
        dest : new file's address
        """
        try:
            if self.name not in listdir(dest) and dest != "*\\*":
                copy2(self.fullPath, dest)
                self.fullPath = dest
        except Exception as e:
            print ("An exception ocurred")

    def cut(self, second_path):
        """
        | This method moves a file from current directory to the second directory.
        :param self : Object
        :param second_path: str
        """
        self.copy(second_path)
        self.delete()

    def delete(self):
        """
        | This method deletes current file.
        :param self: Obj
        """
        # try:
        remove(self.fullPath)
        # except WindowsError:
        #     error_show('The path is invalid', 'listener must add')
        # except Exception:
        #     error_show("An Error happened, please restart the app.", 'listener must add')

    def rename(self, new_name):
        """
        | This method renames current file
        :param self: Obj
        :param new_name:str
        """
        try:
            rename(self.fullPath, ''.join(self.fullPath.split('\\')[:len(self.fullPath) - len(self.type) - len(self.name)]) + new_name)
        except WindowsError:
            error_show('The second directory path is invalid', 'listener must add')
        except Exception:
            error_show("An Error happened, please restart the app.", 'listener must add')


class Directory(object):
    def __init__(self, strAdrs):
        self.fullAddress = strAdrs
        self.list_address = self.fullAddress.split("\\")
        # print ":::::::::::::::::::::::::::::::::::::::::::"
        # print self.list_address
        if strAdrs.split("\\")[-1]:
            self.name = strAdrs.split("\\")[-1]
        else:
            self.name = strAdrs
        self.parent = ""
        if len(self.list_address) > 2:
            for counter in range(len(self.list_address) - 2, -1, -1):
                # print "##########################"
                # print self.list_address[counter]
                if self.list_address[counter]:
                    self.parent = self.list_address[counter]
                    break

    def openf(self):
        file_list = []
        for filename in listdir(self.fullAddress):
            file_list.append(filename)
        return file_list
        
    def copy(self, dest):
        try:
            if self.name not in listdir(dest) and dest != "*\\*":
                dest += "\\" + self.fullAddress.split("\\")[-1]
                copytree(self.fullAddress, dest)
        except Exception as e:
            print e

    def cut(self, dest):
        self.copy(dest)
        self.delete()

    def delete(self):
        """
        | This method deletes current directory and all it's contents.
        :param self: Obj
        """
        try:
            rmtree(self.fullAddress)
        except WindowsError:
            error_show('The path is invalid', 'listener must add')
        except Exception:
            error_show("An Error happened, please restart the app.", 'listener must add')

    def rename(self, new_name):
        """
        | This method renames current directory
        :param self: Obj
        :param new_name:str
        """
        try:
            rename(self.fullAddress, ''.join(self.fullAddress[:len(self.fullAddress) - len(self.name)]) + new_name)
        except WindowsError:
            error_show('The second directory path is invalid', 'listener must add')
        except Exception:
            error_show("An Error happened, please restart the app.", 'listener must add')


class New_File(QtGui.QDialog):
    def __init__(self):
        super(New_File, self).__init__()

        self.path = ''
        
        self.browseButton = self.createButton("&Browse...", self.browse)
        self.quitButton = self.createButton("&Quit",self.close)
        self.findButton = self.createButton("&Create", self.create)

        
        self.fileComboBox = self.createLineEdit()
        self.textComboBox = self.createLineEdit()
        self.directoryComboBox = self.createComboBox(self.path)

        fileLabel = QtGui.QLabel("NameFile:")
        textLabel = QtGui.QLabel("TypeFile:")
        directoryLabel = QtGui.QLabel("In directory:")

        
        self.filesFoundLabel = QtGui.QLabel()
        buttonsLayout = QtGui.QHBoxLayout()
        buttonsLayout.addWidget(self.findButton)
        buttonsLayout.addWidget(self.quitButton)       
        mainLayout = QtGui.QGridLayout()
        mainLayout.addWidget(fileLabel, 0, 0)
        mainLayout.addWidget(self.fileComboBox, 0, 1, 1, 2)
        mainLayout.addWidget(textLabel, 1, 0)
        mainLayout.addWidget(self.textComboBox, 1, 1, 1, 2)
        mainLayout.addWidget(directoryLabel, 2, 0)
        mainLayout.addWidget(self.directoryComboBox, 2, 1)
        mainLayout.addWidget(self.browseButton, 2, 2)
        mainLayout.addWidget(self.filesFoundLabel, 3, 0)
        mainLayout.addLayout(buttonsLayout, 3, 0, 1, 3)
        self.setLayout(mainLayout)

        self.create()
        
        self.setWindowTitle("Create_New_File")
        self.resize(200, 200)


    def browse(self):
        directory = QtGui.QFileDialog.getExistingDirectory(self, "Create_New_File",
                QtCore.QDir.currentPath())
        if directory:
            if self.directoryComboBox.findText(directory) == -1:
                self.directoryComboBox.addItem(directory)
            self.directoryComboBox.setCurrentIndex(self.directoryComboBox.findText(directory))

    
    def create(self):
        Name = self.fileComboBox.text()
        Type = self.textComboBox.text()
        Path = self.directoryComboBox.currentText()

        self.updateComboBox(self.directoryComboBox)
        
        self.item_list = [str(Name), str(Type) , str(Path)]
        item_list = self.item_list

        if self.item_list[1]:
            if self.item_list[0] and self.item_list[-1]:
                file = open(str(self.item_list[-1] + '/' + self.item_list[0] + '.' + self.item_list[1]), 'w')
                file.close() 
        else:
            if self.item_list[0] and self.item_list[-1]:
                mkdir(self.item_list[-1] + '/' + self.item_list[0])

    def updateComboBox(self,comboBox):
        if comboBox.findText(comboBox.currentText()) == -1:
            comboBox.addItem(comboBox.currentText())

    def _NewFile(self ,app ):
            self.show()

    def createButton(self, text, member):
        button = QtGui.QPushButton(text)
        button.clicked.connect(member)
        return button

    def createComboBox(self, text=""):
        comboBox = QtGui.QComboBox()
        comboBox.setEditable(True)
        comboBox.addItem(text)
        return comboBox
  
    def createLineEdit(self, text=""):
        line = QtGui.QLineEdit()
        return line
class New_Dir(QtGui.QDialog):
    def __init__(self):
        super(New_Dir, self).__init__()

        self.path = ''
        
        self.quitButton = self.createButton("&Quit",self.close)
        self.findButton = self.createButton("&Create", self.create)

        
        self.fileComboBox = self.createLineEdit()

        fileLabel = QtGui.QLabel("NameFile:")
        
        self.filesFoundLabel = QtGui.QLabel()
        buttonsLayout = QtGui.QHBoxLayout()
        buttonsLayout.addWidget(self.findButton)
        buttonsLayout.addWidget(self.quitButton)       
        mainLayout = QtGui.QGridLayout()
        mainLayout.addWidget(fileLabel, 0, 0)
        mainLayout.addWidget(self.fileComboBox, 0, 1, 1, 2)
        mainLayout.addWidget(self.filesFoundLabel, 3, 0)
        mainLayout.addLayout(buttonsLayout, 3, 0, 1, 3)
        self.setLayout(mainLayout)

        self.create()
        
        self.setWindowTitle("Create New Dir")
        self.resize(200, 200)

           
    def create(self):
        Name = self.fileComboBox.text()
        self.item_list = [str(Name)]
        item_list = self.item_list
        if self.item_list[0]:
            mkdir(self.path + '/' + self.item_list[0])


    def _NewDir(self ,app ):
        self.show()

    def createButton(self, text, member):
        button = QtGui.QPushButton(text)
        button.clicked.connect(member)
        return button
  
    def createLineEdit(self, text=""):
        line = QtGui.QLineEdit()
        return line

class User_D(QtGui.QDialog):
    def __init__(self):

        super(User_D, self).__init__()

        self.path = ''


        self.quitButton = self.createButton("&Quit",self.close)
        self.SingButton = self.createButton("&SingUp", self.create)


        self.fileComboBox = self.createLineEdit()
        self.textComboBox = self.createLineEdit()


        fileLabel = QtGui.QLabel("Userame:")
        textLabel = QtGui.QLabel("Password:")



        self.filesFoundLabel = QtGui.QLabel()
        buttonsLayout = QtGui.QHBoxLayout()
        buttonsLayout.addWidget(self.SingButton)
        buttonsLayout.addWidget(self.quitButton)
        mainLayout = QtGui.QGridLayout()
        mainLayout.addWidget(fileLabel, 0, 0)
        mainLayout.addWidget(self.fileComboBox, 0, 1, 1, 2)
        mainLayout.addWidget(textLabel, 1, 0)
        mainLayout.addWidget(self.textComboBox, 1, 1, 1, 2)
        mainLayout.addWidget(self.filesFoundLabel, 3, 0)
        mainLayout.addLayout(buttonsLayout, 3, 0, 1, 3)
        self.setLayout(mainLayout)

        self.create()

        self.setWindowTitle("SignUp")
        self.resize(200, 200)


    def create(self):
        User = self.fileComboBox.text()
        Pass = self.textComboBox.text()

        self.item_list = [str(User), str(Pass)]

        #if self.item_list[0] and self.item_list[1]:
         #   send_result("0|" + self.item_list[0] + "|" + self.item_list[1])

    def _User(self ,app , action ):
            self.SingButton.setText(action)
            self.show()

    def createButton(self, text, member):
        button = QtGui.QPushButton(text)
        button.clicked.connect(member)
        return button

    def createLineEdit(self, text=""):
        line = QtGui.QLineEdit()
        return line

class User_S(QtGui.QDialog):
    def __init__(self):

        super(User_S, self).__init__()

        self.path = ''
        self.quitButton = self.createButton("&Quit",self.close)
        self.SingButton = self.createButton("&Ok", self.create)
        # self.fileComboBox = self.createLineEdit()
        self.textComboBox = self.createLineEdit()
        self.text1ComboBox = self.createLineEdit()
        # fileLabel = QtGui.QLabel("Username")
        textLabel = QtGui.QLabel("Server ip")
        text1Label = QtGui.QLabel("Server Port")
        self.server, self.port = "", 0
        self.filesFoundLabel = QtGui.QLabel()
        buttonsLayout = QtGui.QHBoxLayout()
        buttonsLayout.addWidget(self.SingButton)
        buttonsLayout.addWidget(self.quitButton)
        mainLayout = QtGui.QGridLayout()
        # mainLayout.addWidget(fileLabel, 0, 0)
        # mainLayout.addWidget(self.fileComboBox, 0, 1, 1, 2)
        mainLayout.addWidget(textLabel, 1, 0)
        mainLayout.addWidget(self.textComboBox, 1, 1, 1, 2)
        mainLayout.addWidget(text1Label, 2, 0)
        mainLayout.addWidget(self.text1ComboBox, 2, 1, 1, 2)
        mainLayout.addWidget(self.filesFoundLabel, 3, 0)
        mainLayout.addLayout(buttonsLayout, 3, 0, 1, 3)
        self.setLayout(mainLayout)

        #self.create()

        self.setWindowTitle("Setting")
        self.resize(200, 200)


    def _Setting_(self):
            self.show()

    def createButton(self, text, member):
        button = QtGui.QPushButton(text)
        # button.clicked.connect(self.member)
        return button

    def createLineEdit(self, text=""):
        line = QtGui.QLineEdit()
        return line

    def member(self):
        self.server =  self.textComboBox.text()
        self.port = self.text1ComboBox.text()

class User_C(QtGui.QDialog):
    def __init__(self):

        super(User_C, self).__init__()

        self.path = ''


        self.quitButton = self.createButton("&Quit",self.close)
        self.SingButton = self.createButton("&Ok", self.create)


        self.fileComboBox = self.createLineEdit()

        fileLabel = QtGui.QLabel("Username")


        self.filesFoundLabel = QtGui.QLabel()
        buttonsLayout = QtGui.QHBoxLayout()
        buttonsLayout.addWidget(self.SingButton)
        buttonsLayout.addWidget(self.quitButton)
        mainLayout = QtGui.QGridLayout()
        mainLayout.addWidget(fileLabel, 0, 0)
        mainLayout.addWidget(self.fileComboBox, 0, 1, 1, 2)
        mainLayout.addWidget(self.filesFoundLabel, 3, 0)
        mainLayout.addLayout(buttonsLayout, 3, 0, 1, 3)
        self.setLayout(mainLayout)

        #self.create()

        self.setWindowTitle("Setting")
        self.resize(200, 200)


    def _Setting_C(self):
            self.show()

    def createButton(self, text, member):
        button = QtGui.QPushButton(text)
        button.clicked.connect(member)
        return button

    def createLineEdit(self, text=""):
        line = QtGui.QLineEdit()
        return line

class Rename_(QtGui.QDialog):
    def __init__(self):

        super(Rename_, self).__init__()

        self.path = ''


        self.RenameButton = self.createButton("&done",self.create)


        self.fileComboBox = self.createLineEdit()

        fileLabel = QtGui.QLabel("Rename")


        self.filesFoundLabel = QtGui.QLabel()
        buttonsLayout = QtGui.QHBoxLayout()
        buttonsLayout.addWidget(self.RenameButton)
        mainLayout = QtGui.QGridLayout()
        mainLayout.addWidget(fileLabel, 0, 0)
        mainLayout.addWidget(self.fileComboBox, 0, 1, 1, 2)
        mainLayout.addWidget(self.filesFoundLabel, 3, 0)
        mainLayout.addLayout(buttonsLayout, 3, 0, 1, 3)
        self.setLayout(mainLayout)

        self.create()

        self.setWindowTitle("Setting")
        self.resize(200, 200)

    def create(self):

        file_name = self.fileComboBox

        self.item_list = [str(file_name)]

    def rename_(self):
        self.show()

    def createButton(self, text, member):
        button = QtGui.QPushButton(text)
        button.clicked.connect(member)
        return button

    def createLineEdit(self, text=""):
        line = QtGui.QLineEdit()
        return line

# if __name__ == '__main__':
#
#     import sys
#
#     app = QtGui.QApplication(sys.argv)
#     window = NewFile()
#     window.show()
#     sys.exit(app.exec_())
