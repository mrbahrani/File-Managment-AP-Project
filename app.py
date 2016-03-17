from __Classes import *
from DefaultUI import *
from funcs import *
from visual import *

def window():
    # This function is the main window of the application.
   app = QtGui.QApplication(sys.argv)
   #strAddress = "C:\\" # VERY IMPORTANT: Address MUST be finished with "\\". MUST!!
   listDrives = drivers() # VERY IMPORTANT: Address MUST be finished with "\\". MUST!!
   print listDrives
   MainWindow = QtGui.QMainWindow()
   ui = Ui_MainWindow()
   ui.setupUi(MainWindow)
   ui.treeWidget.setHeaderLabels(["Directories"])
   model0 = QtGui.QFileSystemModel()
   model0.setRootPath("/")
   #ui.listView.setModel(model0)
   #root = QtGui.QTreeWidgetItem(ui.treeWidget)
   #root.setText(0,"C")
   #treeView(strAddress,root)
   listRoot = []
   for driver in listDrives:
      tree_widget_item = QtGui.QTreeWidgetItem(ui.treeWidget)
      list_widget_item = QtGui.QListWidgetItem(ui.listView)
      list_widget_item.setText(driver[0].upper())
      icon = QtGui.QIcon('icons/folder.ico')
      list_widget_item.setIcon(icon)
      tree_widget_item.setText(0, driver[0].upper())
      tree_widget_item.setIcon(0, icon)
      tree_widget_item.setIcon(1, icon)
      treeView(driver, tree_widget_item)

   MainWindow.show()
   sys.exit(app.exec_())

if __name__=="__main__":
    window()