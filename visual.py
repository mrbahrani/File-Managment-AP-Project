from __Classes import *
from DefaultUI import *
from funcs import *
#from threading import Thread

def treeView(fullPath,qwtIt):
    #This function visualizes the tree view of the directories
    try:
        dirList= get_directories(fullPath)
        if bool(dirList):
            for it in dirList:
                i = QtGui.QTreeWidgetItem()
                i.setText(0,it)
                qwtIt.addChild(i)

    except WindowsError:
        print("Accsess denied")
    except:
        print("An unwanted exception ocurred!!")
