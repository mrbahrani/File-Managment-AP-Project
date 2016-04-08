"""
history_list is not still ready so the wroten code just print name of the file not it's path
"""
from __Classes import *
from DefaultUI import *
from funcs import *
from visual import *
from navigation import *
from os.path import isdir
from time import sleep

from search import search, step_by_step_search
from events import *
import sys
# add_here('\\')
# add_here('E:\\Music\\')
selected_item = [""]


class MainWindow(QtGui.QMainWindow, New_File,New_Dir ,User_D):
    index = 1
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowIcon(QtGui.QIcon('icons\\mycomputer.ico'))
        self.New_File = New_File()
        self.ui = Ui_MainWindow()
        self.New_File = New_File()
        self.New_Dir = New_Dir()
        self.User_D= User_D()
        self.ui.setupUi(self)
        self.add_actions()
        self.setup()

        
        self.memory_list = []
        self.list = list()
        self.list_ = list()
        
        self.setAcceptDrops(True)
        self.ui.listView.setDragEnabled(True)
        self.ui.listView.setDragDropMode(QtGui.QAbstractItemView.InternalMove)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()
        else:
          super(MainWindow, self).dragEnterEvsent(event)

    def dragMoveEvent(self, event):
        super(MainWindow, self).dragMoveEvent(event)

    def dropEvent(self, event):
        self.list = list()
        self.list_ = list()
        self.memory_list = []
        if event.mimeData().hasUrls():
            for url in event.mimeData().urls():
                self.list.append(str(url.path()))
                print self.list , 21
            event.acceptProposedAction()
            self.list_ = self.list[0].split('/')
            print self.list_ ,self.list
                                                                                     
            self.copy_action_(self.list_[-1],(self.list[0])[2:])

            self.paste_action_(history_list[here[0]][0], self.ui.listView)
            
        else:
            self.ui.listView.dropEvent(event)    
 


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
        self.ui.listView.itemClicked.connect(self.selected_saver)

        #self.ui.pushButton.clicked.connect(self.up)
        self.ui.pushButton.clicked.connect(lambda: self.ui.contextMenuEvent())

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Return:
            if self.ui.listView.currentItem():
                list_Dclicked(history_list[here[0]][0], str(self.ui.listView.currentItem().text()), self.ui.listView, self.ui.lineEdit)

    def contextMenuEvent(self , event):
        print selected_item
        self.menu = QtGui.QMenu(self)
        if selected_item[0] != "" :
            open_actio = QtGui.QAction("Open",self)
            open_actio.triggered.connect(lambda: list_Dclicked(history_list[here[0]][0], str(self.ui.listView.currentItem().text()),self.ui.listView,self.ui.lineEdit))
            self.menu.addAction(open_actio)

            if isdir( str(history_list[here[0]][0]) + "\\" + str(selected_item[0]) ) :
                open_innew_actio = QtGui.QAction("Open in new window",self)
                open_innew_actio.triggered.connect(self.copy)
                self.menu.addAction(open_innew_actio)

            copy_actio = QtGui.QAction("Copy",self)
            copy_actio.triggered.connect(self.copy)
            self.menu.addAction(copy_actio)

            cut_actio = QtGui.QAction("Cut",self)
            cut_actio.triggered.connect(self.cut)
            self.menu.addAction(cut_actio)

        paste_actio = QtGui.QAction("Paste",self)
        paste_actio.triggered.connect(self.paste)
        self.menu.addAction(paste_actio)

        if selected_item[0] != "" :

            delete_actio = QtGui.QAction("Delete",self)
            delete_actio.triggered.connect(self.delete)
            self.menu.addAction(delete_actio)

            rename_actio = QtGui.QAction("Rename",self)
            rename_actio.triggered.connect(self.copy)
            self.menu.addAction(rename_actio)

        self.menu.popup(QtGui.QCursor.pos())


    def add_actions(self):
        """
        | This method adds all slots of actions of menu bar elements
        """
        self.ui.actionCopy.triggered.connect(self.copy)
        self.ui.actionCut.triggered.connect(self.cut)
        self.ui.actionNewFile.triggered.connect(self.NewFile)
        self.ui.actionNewDir.triggered.connect(self.NewDir)
        self.ui.actionSingUp.triggered.connect(self.User)
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
        delete_action(item[0], history_list[here[0]][0], serlf.ui.listView)

    def search(self, item):
        add_here(history_list[here[0]][0])
        result = search(str(item), history_list[here[0]][0])
        print "result"
        print result
        if not result:
            result = step_by_step_search(str(item), history_list[here[0]][0])
        if result:
            self.ui.listView.clear()
            listView(result, self.ui.listView)
            add_here("*\\*", history_list, here, "*")

    def NewDir(self):
        self.New_Dir._NewDir(self)

    def NewFile(self):
        self.New_File._NewFile(self)

    def copy_action_(self ,file_name, current_directory):
        """
        | This function saves a list of files those must copy to another directory to the memory list
        copy_action(files_names, current_directory[, memory_list=memory])
        :param file_name:str
        :param current_directory:str
        :param memory_list:list
        """
        self.memory_list = [0 , self.list[0][1:]]
        print self.memory_list , file_name , current_directory , 1234
        if file_name:
            return self.memory_list

    def paste_action_(self ,current_directory, list_widget):
        # print "PASTE"
        """
        | This function will paste(copy or cut) all elements are in the memory list.
        paste(current_directory[, memory_list=memory])
        :param current_directory:str
        :param list_widget:QListWidget
        :param memory_list:list
        """
        print self.memory_list , current_directory , 516165
        #memory_list[1] = ((memory_list[-1].split('\\'))[0])
        if self.memory_list:
            if not self.memory_list[0]:
                if isdir(self.memory_list[1]):
                    directory = Directory(self.memory_list[1])
                    directory.copy(current_directory)
                else:
                    file_object = File(self.memory_list[1])
                    file_object.copy(current_directory)    

    def User(self):
        self.User_D._User(self)

class Updator(QtCore.QThread):
    def __init__(self,MainWindow):
        super(Updator,self).__init__()
        self.MainWindow = MainWindow
    def run(self):

        oldList = list()
        newListF= list()
        newListD= list()
        while True:
            sleep(0.01)
            lLock.acquire()
            if history_list[here[0]][0]=="":
                newListD = list()
                newListF = list()
            else:
                newListD = get_directories(history_list[here[0]][0])
                newListF = get_files(history_list[here[0]][0])
            ctr = self.MainWindow.ui.listView.count()
            for itr in range(ctr):
                oldList += [str(self.MainWindow.ui.listView.item(itr).text())]
            # *********************************
            for itrF in newListF:
                if not (itrF in oldList):
                    item = QtGui.QListWidgetItem()
                    item.setText(itrF)
                    icon = QtGui.QIcon(file_icon(itrF))
                    item.setIcon(icon)
                    print oldList,"*****"
                    self.MainWindow.ui.listView.addItem(item)
            for itrD in newListD:
                if not (itrD in oldList):
                    item = QtGui.QListWidgetItem()
                    item.setText(itrD)
                    icon = QtGui.QIcon("icons\\folder.ico")
                    item.setIcon(icon)
                    self.MainWindow.ui.listView.addItem(item)
            # *********************************
            if history_list[here[0]][0]=="":
                newListD = list()
                newListF = list()
            else:
                newListD = get_directories(history_list[here[0]][0])
                newListF = get_files(history_list[here[0]][0])
            ommitList = list()
            for itr in oldList:
                if not (itr in newListD+newListF):
                    ommitList += [itr]
            num_of_items = self.MainWindow.ui.listView.count()
            holder = 0
            while holder <num_of_items:
                if str(self.MainWindow.ui.listView.item(holder).text()) in ommitList:
                    self.MainWindow.ui.listView.takeItem(holder)
                    num_of_items -=1
                else:
                    holder +=1
            # *********************************
            oldList = list()
            lLock.release()

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    Win = MainWindow()
    updator = Updator(Win)
    updator.start()
    Win.start_show(app)
