from os import rename, access, remove, R_OK, F_OK, startfile, listdir
from __ErrorHandler import error_show
from __exceptions import FileNotExist,NoPermission
from shutil import rmtree, copy2, copytree
from PyQt4 import QtCore, QtGui
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
        try:
            rename(self.fullPath, second_path)
            self.delete()
        except WindowsError:
            error_show('The second directory path is invalid', 'listener must add')
        except Exception:
            error_show("An Error happened, please restart the app.", 'listener must add')

    def delete(self):
        """
        | This method deletes current file.
        :param self: Obj
        """
        try:
            remove(self.fullPath)
        except WindowsError:
            error_show('The path is invalid', 'listener must add')
        except Exception:
            error_show("An Error happened, please restart the app.", 'listener must add')

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
        print ":::::::::::::::::::::::::::::::::::::::::::"
        print self.list_address
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
        print self.parent
        print ";;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;"
    def openf(self):
        file_list = []
        for filename in listdir(self.fullAddress):
            file_list.append(filename)
        return file_list
        
    def copy(self, dest):
        dest += self.fullAddress.split("\\")[-1]
        copytree(self.fullAddress, dest)

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
    def __init__(self, parent=None):
        super(New_File, self).__init__(parent)
        
        self.browseButton = self.createButton("&Browse...", self.browse)
        self.findButton = self.createButton("&Create", self.create)

        
        self.fileComboBox = self.createComboBox()
        self.textComboBox = self.createComboBox()
        self.directoryComboBox = self.createComboBox(QtCore.QDir.currentPath())

        fileLabel = QtGui.QLabel("NameFile:")
        textLabel = QtGui.QLabel("TypeFile:")
        directoryLabel = QtGui.QLabel("In directory:")

        
        self.filesFoundLabel = QtGui.QLabel()
        buttonsLayout = QtGui.QHBoxLayout()
        buttonsLayout.addWidget(self.findButton)
        mainLayout = QtGui.QGridLayout()
        mainLayout.addWidget(fileLabel, 0, 0)
        mainLayout.addWidget(self.fileComboBox, 0, 1, 1, 2)
        mainLayout.addWidget(textLabel, 1, 0)
        mainLayout.addWidget(self.textComboBox, 1, 1, 1, 2)
        mainLayout.addWidget(directoryLabel, 2, 0)
        mainLayout.addWidget(self.directoryComboBox, 2, 1)
        mainLayout.addWidget(self.browseButton, 2, 2)
        mainLayout.addWidget(self.filesFoundLabel, 4, 0)
        mainLayout.addLayout(buttonsLayout, 5, 0, 1, 3)
        self.setLayout(mainLayout)

        self.create()
        
        self.setWindowTitle("Create_New_File")
        self.resize(500, 300)

    def browse(self):
        directory = QtGui.QFileDialog.getExistingDirectory(self, "Create_New_File",
                QtCore.QDir.currentPath())
        if directory:
            if self.directoryComboBox.findText(directory) == -1:
                self.directoryComboBox.addItem(directory)
            self.directoryComboBox.setCurrentIndex(self.directoryComboBox.findText(directory))

    def create(self):
        Name = self.fileComboBox.currentText()
        Type = self.textComboBox.currentText()
        Path = self.directoryComboBox.currentText()

        self.updateComboBox(self.fileComboBox)
        self.updateComboBox(self.textComboBox)
        self.updateComboBox(self.directoryComboBox)
        
        self.item_list = [str(Name), str(Type) , str(Path)]
        item_list = self.item_list
        
        if self.item_list[0] and self.item_list[1] and self.item_list[-1]:
            file = open(str(self.item_list[-1] + '/' + self.item_list[0] + '.' + self.item_list[1]), 'w')
            file.close() 
    
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
        comboBox.setSizePolicy(QtGui.QSizePolicy.Expanding,
                QtGui.QSizePolicy.Preferred)
        return comboBox

# if __name__ == '__main__':
#
#     import sys
#
#     app = QtGui.QApplication(sys.argv)
#     window = NewFile()
#     window.show()
#     sys.exit(app.exec_())
