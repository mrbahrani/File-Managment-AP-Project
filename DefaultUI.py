# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'defaultUI4.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import sys

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(756, 590)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_3 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        # self.groupBox.setMaximumSize(QtCore.QSize(738, 16777215))
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout = QtGui.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.pushButton_2 = QtGui.QPushButton(self.groupBox)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.gridLayout.addWidget(self.pushButton_2, 0, 0, 1, 1)
        self.lineEdit = QtGui.QLineEdit(self.groupBox)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.gridLayout.addWidget(self.lineEdit, 0, 4, 1, 1)
        self.pushButton = QtGui.QPushButton(self.groupBox)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout.addWidget(self.pushButton, 0, 1, 1, 1)
        self.lineEdit_2 = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.gridLayout.addWidget(self.lineEdit_2, 0, 6, 1, 2)
        self.pushButton_3 = QtGui.QPushButton(self.groupBox)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.gridLayout.addWidget(self.pushButton_3, 0, 2, 1, 1)
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setLocale(QtCore.QLocale(QtCore.QLocale.Persian, QtCore.QLocale.Iran))
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 8, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox, 0, 0, 1, 12)
        self.treeWidget = QtGui.QTreeWidget(self.centralwidget)
        self.treeWidget.setAutoFillBackground(True)
        self.treeWidget.setStyleSheet(_fromUtf8("background:#fff;"))
        self.treeWidget.setLocale(QtCore.QLocale(QtCore.QLocale.Persian, QtCore.QLocale.Iran))
        self.treeWidget.setObjectName(_fromUtf8("treeWidget"))
        self.treeWidget.headerItem().setText(0, _fromUtf8("1"))
        self.gridLayout_3.addWidget(self.treeWidget, 2, 0, 1, 11)
        self.listView = QtGui.QListWidget(self.centralwidget)
        self.listView.setObjectName(_fromUtf8("ListView"))
        self.gridLayout_3.addWidget(self.listView, 2, 11, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 756, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuEdit = QtGui.QMenu(self.menubar)
        self.menuEdit.setObjectName(_fromUtf8("menuEdit"))
        self.menuView = QtGui.QMenu(self.menubar)
        self.menuView.setObjectName(_fromUtf8("menuView"))
        self.menuView_mode = QtGui.QMenu(self.menuView)
        self.menuView_mode.setObjectName(_fromUtf8("menuView_mode"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
       # self.menuVirtual = QtGui.QMenu(self.menubar)
        #self.menuVirtual.setObjectName(_fromUtf8("menuVirtual"))
        #self.menuShell = QtGui.QMenu(self.menubar)
        #self.menuShell.setObjectName(_fromUtf8("menuShell"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew_directory = QtGui.QAction(MainWindow)
        self.actionNew_directory.setObjectName(_fromUtf8("actionNew_directory"))
        self.actionNewFile = QtGui.QAction(MainWindow)
        self.actionNewFile.setObjectName(_fromUtf8("actionNewFile"))
        self.actionCopy = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("icons\\edit_menu_copy.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.actionCopy.setIcon(icon)
        self.actionCopy.setObjectName(_fromUtf8("actionCopy"))
        self.actionCut = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("icons\\edit_menu_cut.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.actionCut.setIcon(icon)
        self.actionCut.setObjectName(_fromUtf8("actionCut"))
        self.actionPaste = QtGui.QAction(MainWindow)
        self.actionPaste.setObjectName(_fromUtf8("actionPaste"))
        self.actionDelete = QtGui.QAction(MainWindow)
        self.actionDelete.setObjectName(_fromUtf8("actionDelete"))
        self.actionUndo = QtGui.QAction(MainWindow)
        self.actionUndo.setObjectName(_fromUtf8("actionUndo"))
        self.actionFind = QtGui.QAction(MainWindow)
        self.actionFind.setObjectName(_fromUtf8("actionFind"))
        self.actionTutorial = QtGui.QAction(MainWindow)
        self.actionTutorial.setObjectName(_fromUtf8("actionTutorial"))
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.actionExtra_large_icons = QtGui.QAction(MainWindow)
        self.actionExtra_large_icons.setObjectName(_fromUtf8("actionExtra_large_icons"))
        self.actionExtra_large_icon = QtGui.QAction(MainWindow)
        self.actionExtra_large_icon.setObjectName(_fromUtf8("actionExtra_large_icon"))
        self.actionLarge_icons = QtGui.QAction(MainWindow)
        self.actionLarge_icons.setObjectName(_fromUtf8("actionLarge_icons"))
        self.actionMedium_icons = QtGui.QAction(MainWindow)
        self.actionMedium_icons.setObjectName(_fromUtf8("actionMedium_icons"))
        self.actionSmall_icons = QtGui.QAction(MainWindow)
        self.actionSmall_icons.setObjectName(_fromUtf8("actionSmall_icons"))
        self.actionList = QtGui.QAction(MainWindow)
        self.actionList.setObjectName(_fromUtf8("actionList"))
        self.actionNew_directory_2 = QtGui.QAction(MainWindow)
        self.actionNew_directory_2.setObjectName(_fromUtf8("actionNew_directory_2"))
       # self.actionVirtual_drive = QtGui.QAction(MainWindow)
        #self.actionVirtual_drive.setObjectName(_fromUtf8("actionVirtual_drive"))
       # self.actionOpen_shell = QtGui.QAction(MainWindow)
        #self.actionOpen_shell.setObjectName(_fromUtf8("actionOpen_shell"))
        #self.actionRestart_shell = QtGui.QAction(MainWindow)
        #self.actionRestart_shell.setObjectName(_fromUtf8("actionRestart_shell"))
        #self.menuFile.addAction(self.actionNew_directory)
        self.menuFile.addAction(self.actionNewFile)
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionCut)
        self.menuEdit.addAction(self.actionPaste)
        self.menuEdit.addAction(self.actionDelete)
        self.menuEdit.addAction(self.actionUndo)
        self.menuEdit.addAction(self.actionFind)
        self.menuView_mode.addAction(self.actionExtra_large_icon)
        self.menuView_mode.addAction(self.actionLarge_icons)
        self.menuView_mode.addAction(self.actionMedium_icons)
        self.menuView_mode.addAction(self.actionSmall_icons)
        self.menuView_mode.addAction(self.actionList)
        self.menuView.addAction(self.menuView_mode.menuAction())
        self.menuHelp.addAction(self.actionTutorial)
        self.menuHelp.addAction(self.actionAbout)
        #self.menuVirtual.addAction(self.actionNew_directory_2)
        #self.menuVirtual.addAction(self.actionVirtual_drive)
        #self.menuVirtual.addSeparator()
        #self.menuShell.addAction(self.actionOpen_shell)
        #self.menuShell.addAction(self.actionRestart_shell)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        #self.menubar.addAction(self.menuShell.menuAction())
        #self.menubar.addAction(self.menuVirtual.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.pushButton_2.setText(_translate("MainWindow", "Back", None))
        self.pushButton_2.setShortcut(_translate("MainWindow", "Alt+Left", None))
        self.pushButton.setText(_translate("MainWindow", "Up", None))
        self.pushButton_3.setText(_translate("MainWindow", "Forward", None))
        self.pushButton_3.setShortcut(_translate("MainWindow", "Alt+Right", None))
        self.pushButton.setShortcut(_translate("MainWindow", "Alt+Up", None))
        self.label.setText(_translate("MainWindow", "Search", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit", None))
        self.menuView.setTitle(_translate("MainWindow", "View", None))
        self.menuView_mode.setTitle(_translate("MainWindow", "View mode", None))
        self.menuHelp.setTitle(_translate("MainWindow", "Help", None))
       # self.menuVirtual.setTitle(_translate("MainWindow", "Virtual", None))
        #self.menuShell.setTitle(_translate("MainWindow", "Shell", None))
        self.actionNew_directory.setText(_translate("MainWindow", "New directory", None))
        self.actionNewFile.setText(_translate("MainWindow", "NewFile", None))
        self.actionCopy.setText(_translate("MainWindow", "Copy", None))
        # The Line below adds shortcut to the action
        self.actionCopy.setShortcut(_translate("MainWindow", "Ctrl+C", None))
        self.actionCut.setText(_translate("MainWindow", "Cut", None))
        # The Line below adds shortcut to the action
        self.actionCut.setShortcut(_translate("MainWindow", "Ctrl+X", None))
        self.actionPaste.setText(_translate("MainWindow", "Paste", None))
        # The Line below adds shortcut to the action
        self.actionPaste.setShortcut(_translate("MainWindow", "Ctrl+V", None))
        self.actionDelete.setText(_translate("MainWindow", "Delete", None))
        self.actionDelete.setShortcut(_translate("MainWindow", "Delete", None))
        self.actionUndo.setText(_translate("MainWindow", "Undo", None))
        self.actionFind.setText(_translate("MainWindow", "Find", None))
        self.actionTutorial.setText(_translate("MainWindow", "Tutorial", None))
        self.actionAbout.setText(_translate("MainWindow", "About", None))
        self.actionExtra_large_icons.setText(_translate("MainWindow", "Extra large icons", None))
        self.actionExtra_large_icon.setText(_translate("MainWindow", "Extra large icons", None))
        self.actionLarge_icons.setText(_translate("MainWindow", "Large icons", None))
        self.actionMedium_icons.setText(_translate("MainWindow", "Medium icons", None))
        self.actionSmall_icons.setText(_translate("MainWindow", "Small icons", None))
        self.actionList.setText(_translate("MainWindow", "List", None))
        self.actionNew_directory_2.setText(_translate("MainWindow", "New directory", None))
        #self.actionVirtual_drive.setText(_translate("MainWindow", "Virtual drive", None))
     #   self.actionOpen_shell.setText(_translate("MainWindow", "Open shell", None))
      #  self.actionRestart_shell.setText(_translate("MainWindow", "Restart shell", None))


#class ExampleApp(QtGui.QMainWindow, Ui_MainWindow):
 #  def __init__(self):
 #       # Explaining super is out of the scope of this article
  #      # So please google it if you're not familar with it
     # Simple reason why we use it here is that it allows us to
        # access variables, methods etc in the design.py file
     #   super(self.__class__, self).__init__()
      #  self.setupUi(self)  # This is defined in design.py file automatically
                            # It sets up layout and widgets that are defined



def main():
    app = QtGui.QApplication(sys.argv)  # A new instance of QApplication
    form = ExampleApp()                 # We set the form to be our ExampleApp (design)
    form.show()                         # Show the form
    app.exec_()                         # and execute the app


if __name__ == '__main__':              # if we're running file directly and not importing it
    main()
