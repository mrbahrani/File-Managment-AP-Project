from __Classes import *
from DefaultUI import *
from funcs import *
from visual import *
from navigation import *
from os.path import isdir
add_here('\\')


class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.setup()

    def setup(self):
        self.ui.setupUi(self)
        self.ui.treeWidget.setHeaderLabels(["Directories"])
        model0 = QtGui.QFileSystemModel()
        model0.setRootPath("/")
        self.icon = QtGui.QIcon('icons/driver.ico')
        for driver in drivers():
            tree_widget_item = QtGui.QTreeWidgetItem(self.ui.treeWidget)
            tree_widget_item.setText(0, driver[0])
            tree_widget_item.setIcon(0, self.icon)
            tree_widget_item.setIcon(1, self.icon)

            treeView(driver, tree_widget_item)
        for i in listdir('C:\\Python27\\'):
            list_widget_item = QtGui.QListWidgetItem(self.ui.listView)
            list_widget_item.setText(i)
            if isdir('C:\\Python27\\' + i):
                list_widget_item.setIcon(self.icon)
            else:
                list_widget_item.setIcon(QtGui.QIcon('icons/text.ico'))
        self.ui.listView.itemClicked.connect(self.printer)

    def printer(self, item):
        print item.text()

    def start_show(self, app):
        self.show()
        sys.exit(app.exec_())


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    Win = MainWindow()
    Win.start_show(app)
