from __Classes import *
from DefaultUI import *
from funcs import *
from visual import *

def window():
    # This function is the main window of the application.
   app = QtGui.QApplication(sys.argv)
   strAddress = "C:\\" # VERY IMPORTANT: Address MUST be finished with "\\". MUST!!
   MainWindow = QtGui.QMainWindow()
   ui = Ui_MainWindow()
   ui.setupUi(MainWindow)
   ui.treeWidget.setHeaderLabels(["Directories"])
   model0 = QtGui.QFileSystemModel()
   model0.setRootPath("/")
   ui.columnView.setModel(model0)
   root = QtGui.QTreeWidgetItem(ui.treeWidget)
   root.setText(0,"C")
   treeView(strAddress,root)


   MainWindow.show()
   sys.exit(app.exec_())

if __name__=="__main__":
    window()