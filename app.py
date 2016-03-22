from __Classes import *
from DefaultUI import *
from funcs import *
from visual import *
from navigation import *
from os.path import isdir
from events import *
add_here('\\')
selected_item = [""]


class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowIcon(QtGui.QIcon('icons\\mycomputer.ico'))
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.add_actions()
        self.setup()

    def setup(self):
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
        for i in listdir('E:\\Music\\'):
            list_widget_item = QtGui.QListWidgetItem(self.ui.listView)
            list_widget_item.setText(i)
            if isdir('E:\\Music\\' + i):
                list_widget_item.setIcon(self.icon)
            else:
                list_widget_item.setIcon(QtGui.QIcon(file_icon(i)))
        self.ui.listView.itemClicked.connect(self.selected_saver)

    def add_actions(self):
        """
        | This method adds all slots of actions of menu bar elements
        """
        self.ui.actionCopy.triggered.connect(self.copy)
        self.ui.actionCut.triggered.connect(self.cut)

    def selected_saver(self, item, selected_item_list=selected_item):
        """
        | This method saves text of selected item into the selected_item list
         selected_saver(self, item[, selected_item_list=selected_item])
         :param item:Object
         :param selected_item_list:list
        """
        selected_item_list.pop()
        selected_item_list.append(str(item.text()))
        print type(selected_item[0])

    def start_show(self, app):
        self.show()
        sys.exit(app.exec_())

    def copy(self, action, item=selected_item):
        copy_action(item, 'E:\\Music\\')
        print memory

    def cut(self, action, item=selected_item):
        cut_action(item, 'E:\\Music\\')
        print memory

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    Win = MainWindow()
    Win.start_show(app)
