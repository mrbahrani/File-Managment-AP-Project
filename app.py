"""
history_list is not still ready so the wroten code just print name of the file not it's path
"""
from __Classes import *
from DefaultUI import *
from funcs import *
from visual import *
from navigation import *
from os.path import isdir

from search import search, step_by_step_search
from events import *
import sys
# add_here('\\')
# add_here('E:\\Music\\')
selected_item = [""]


class MainWindow(QtGui.QMainWindow, New_File):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowIcon(QtGui.QIcon('icons\\mycomputer.ico'))
        self.New_File = New_File()
        self.ui = Ui_MainWindow()
        self.New_File = New_File()
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
            tree_widget_item.dir = driver[0]+":\\"
            tree_widget_item.isUsed =False

            treeView(driver, tree_widget_item)
        for driver in drivers():
            list_widget_item = QtGui.QListWidgetItem(self.ui.listView)
            list_widget_item.setIcon(QtGui.QIcon('icons\\mycomputer.ico'))
            list_widget_item.setText(driver)
        self.ui.treeWidget.itemClicked.connect(self.treeWidget_itemClicked)
        self.ui.listView.itemClicked.connect(self.selected_saver)
        self.ui.treeWidget.itemExpanded.connect(treeWidget_itemExpanded)
        if history_list[here[0]][0] != "*":
            self.ui.listView.doubleClicked.connect(lambda: list_Dclicked(history_list[here[0]][0], str(self.ui.listView.currentItem().text()),self.ui.listView,self.ui.lineEdit))

        #self.ui.pushButton.clicked.connect(self.up)
        self.ui.pushButton.clicked.connect(lambda : self.ui.contextMenuEvent())
    # def keyPressEvent(self, event):
    #     if event.key() == QtCore.Qt.Key_Enter or QtCore.Qt.Key_Return:
    #           self.ui.listView.doubleClicked.connect(lambda: list_Dclicked(history_list[here[0]][0], str(self.ui.listView.currentItem().text()),self.ui.listView))

    def contextMenuEvent(self , event):
        self.menu = QtGui.QMenu(self)
        copy_actio = QtGui.QAction("Copy",self)
        copy_actio.triggered.connect(self.copy)
        self.menu.addAction(copy_actio)

        cut_actio = QtGui.QAction("Cut",self)
        cut_actio.triggered.connect(self.cut)
        self.menu.addAction(cut_actio)

        paste_actio = QtGui.QAction("Paste",self)
        paste_actio.triggered.connect(self.paste)
        self.menu.addAction(paste_actio)

        delete_actio = QtGui.QAction("Delete",self)
        delete_actio.triggered.connect(self.delete)
        self.menu.addAction(delete_actio)

        self.menu.popup(QtGui.QCursor.pos())

    def Pr(self):
        print "sssss"

    def add_actions(self):
        """
        | This method adds all slots of actions of menu bar elements
        """
        self.ui.actionCopy.triggered.connect(self.copy)
        self.ui.actionCut.triggered.connect(self.cut)
        self.ui.actionNewFile.triggered.connect(self.NewFile)
        self.ui.actionPaste.triggered.connect(self.paste)
        self.ui.actionDelete.triggered.connect(self.delete)
        # self.ui.pushButton_3.clicked.connect(self.forward)
        self.ui.pushButton_2.clicked.connect(lambda: history_back(self.ui))
        self.ui.pushButton_3.clicked.connect(lambda: history_forward(self.ui))
        self.ui.lineEdit_2.returnPressed.connect(lambda: self.search(self.ui.lineEdit_2.text()))


    def selected_saver(self, item, selected_item_list=selected_item):
        """
        | This method saves text of selected item into the selected_item list
         selected_saver(self, item[, selected_item_list=selected_item])
         :param item:Object
         :param selected_item_list:list
        """
        selected_item_list.pop()
        selected_item_list.append(str(item.text()))
        # print type(selected_item[0])
        # self.ui.lineEdit.setText(selected_item[0])

    def treeWidget_itemClicked(self, itemList, selected_item):
        self.ui.lineEdit.setText(self.ui.treeWidget.currentItem().dir)
        self.ui.listView.clear()
        add_here(self.ui.treeWidget.currentItem().dir)
        listView(self.ui.treeWidget.currentItem().dir, self.ui.listView)


    def up(self,h_list=history_list):
        try:
            this_dir = history_list[here[0]][0]
            list_dir = this_dir.split("\\")
            p_dir = ""
            for i in range(len(list_dir)-2):
                p_dir = p_dir + list_dir[i] + "\\"
            add_here(p_dir)
            self.ui.lineEdit.setText(p_dir)
            self.ui.listView.clear()
            listView(p_dir,self.ui.listView)
        except  IndexError :
            return False

    def start_show(self, app):
        self.show()
        sys.exit(app.exec_())

    def copy(self, action, item=selected_item):
        """
        | This method calls copy_action function for selected item
        :param action:QAction
        :param item:list
        """
        copy_action(item[0], history_list[here[0]][0])

    def NewFile(self):
        self.New_File._NewFile(self)

    def cut(self, action, item=selected_item):
        """
        | This method calls cut_action function for selected item
        :param action:QAction
        :param item:list
        """
        cut_action(item[0], history_list[here[0]][0])

    def paste(self, action):
        """
        | This function calls paste_action function for current directory. Before that it'll clear QListWidget
        :param action:QAction
        """
        self.ui.listView.clear()                    # This line clears QListWidget
        paste_action(history_list[here[0]][0], self.ui.listView)

    def delete(self, action, item=selected_item):
        self.ui.listView.clear()
        delete_action(item[0], history_list[here[0]][0], self.ui.listView)

    def search(self, item):
        add_here(history_list[here[0]][0])
        result = search(str(item), history_list[here[0]][0])
        print "result"
        print result
        if not result:
            result = step_by_step_search(str(item), history_list[here[0]][0])
        self.ui.listView.clear()
        listView(result, self.ui.listView)
        if result:
            add_here("*\\*", history_list, here, "*")

    def NewFile(self):
        self.New_File._NewFile(self)

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    Win = MainWindow()
    Win.start_show(app)
