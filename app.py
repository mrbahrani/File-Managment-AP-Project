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
   for rt in listDrives:
      i = QtGui.QTreeWidgetItem(ui.treeWidget)
      i.setText(0,rt[0].upper())
      treeView(rt,i)



   MainWindow.show()
   sys.exit(app.exec_())

if __name__=="__main__":
    window()