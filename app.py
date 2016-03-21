from __Classes import *
from DefaultUI import *
from funcs import *
from visual import *
from navigation import *
from os.path import isdir
add_here('\\')


def window():
    # This function is the main window of the application.
    app = QtGui.QApplication(sys.argv)
    # strAddress = "C:\\" # VERY IMPORTANT: Address MUST be finished with "\\". MUST!!
    listDrives = drivers()     # VERY IMPORTANT: Address MUST be finished with "\\". MUST!!
    print listDrives
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.treeWidget.setHeaderLabels(["Directories"])
    model0 = QtGui.QFileSystemModel()
    model0.setRootPath("/")
    # ui.listView.setModel(model0)
    # root = QtGui.QTreeWidgetItem(ui.treeWidget)
    # root.setText(0,"C")
    # treeView(strAddress,root)
    list_root = []
    icon = QtGui.QIcon('icons/driver.ico')
    for driver in listDrives:
        tree_widget_item = QtGui.QTreeWidgetItem(ui.treeWidget)
        tree_widget_item.setText(0, driver[0])
        tree_widget_item.setIcon(0, icon)
        tree_widget_item.setIcon(1, icon)
        treeView(driver, tree_widget_item)
    for i in listdir('C:\\Python27\\'):
        list_widget_item = QtGui.QListWidgetItem(ui.listView)
        list_widget_item.setText(i)
        if isdir('C:\\Python27\\' + i):
            list_widget_item.setIcon(icon)
        else:
            list_widget_item.setIcon(QtGui.QIcon('icons/text.ico'))
    MainWindow.show()
    sys.exit(app.exec_())

if __name__=="__main__":
    window()