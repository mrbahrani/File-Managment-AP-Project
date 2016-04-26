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
from copy import deepcopy,copy
from search import search, search_list
from events import *
from Socket.SocketUI import *
from Socket.Client import *
from Socket.db import set_setting
from Socket.funcssock import *
import sys
from threading import Thread
from subprocess import Popen
# add_here('\\')
# add_here('E:\\Music\\')
selected_item = [""]


class MainWindow(QtGui.QMainWindow, New_File,New_Dir ,User_l, User_SU , User_S , User_C):
    index = 0

    def __init__(self):
        super(MainWindow, self).__init__()
        self.window_index = MainWindow.index
        MainWindow.prepare_indexes()
        self.setWindowIcon(QtGui.QIcon('icons\\mycomputer.ico'))
        self.sub_proccess = ''
        self.server_is_run = False
        self.New_File = New_File()
        self.ui = Ui_MainWindow()
        self.New_File = New_File()
        self.New_Dir = New_Dir()
        self.Rename = Rename_()
        self.User_l = User_l()
        self.User_SU = User_SU()
        self.User_S = User_S()
        self.User_C = User_C()
        self.ui.setupUi(self)
        self.add_actions()
        self.setup()
        winList.append(self)

        self.memory_list = []

        self.list = []
        self.list_ = []

        self.dragOver = False
        self.setAcceptDrops(True)
        self.ui.listView.setDragEnabled(True)
        self.ui.listView.setDragDropMode(QtGui.QAbstractItemView.InternalMove)

    @classmethod
    def prepare_indexes(self):
        MainWindow.index += 1
        history_list.append([["", ""]])
        here.append([0])

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()
        else:
          super(MainWindow, self).dragEnterEvsent(event)

    def dragMoveEvent(self, event):
        super(MainWindow, self).dragMoveEvent(event)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
         #   event.acceptProposedAction()
        #else:
            #print event
            #self.ui.listView.dragEnterEvsent(event)
            event.setAccepted(True)
            self.dragOver = True
            self.update()
        else:
            event.setAccepted(False)

    def dragMoveEvent(self, event):
        super(MainWindow, self).dragMoveEvent(event)


    def dropEvent(self, event):
        self.list = list()
        self.list_ = list()
        self.memory_list = []
        if event.mimeData().hasUrls():
            for url in event.mimeData().urls():
                self.list.append(str(url.path()))
                # print self.list , 21
            event.acceptProposedAction()
            self.list_ = self.list[0].split('/')
            # print self.list_ ,self.list

            self.copy_action_(self.list_[-1],(self.list[0])[2:])

            self.paste_action_(history_list[self.window_index][here[self.window_index][0]][0], self.ui.listView)

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
        print history_list
        print here
        if history_list[self.window_index][here[self.window_index][0]][0] != "*":
            self.ui.listView.doubleClicked.connect(lambda: list_Dclicked(history_list[self.window_index][here[self.window_index][0]][0], str(self.ui.listView.currentItem().text()), self.ui.listView, self.ui.lineEdit, self.window_index))
        self.ui.listView.itemClicked.connect(self.selected_saver)

        self.ui.pushButton.clicked.connect(self.up)
        #self.ui.pushButton.clicked.connect(lambda: self.ui.contextMenuEvent())

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Return:
            if self.ui.listView.currentItem():
                list_Dclicked(history_list[self.window_index][here[self.window_index][0]][0], str(self.ui.listView.currentItem().text()), self.ui.listView, self.ui.lineEdit,self.window_index)

    def contextMenuEvent(self , event):
        # print selected_item
        self.menu = QtGui.QMenu(self)
        if selected_item[0] != "" :
            open_actio = QtGui.QAction("Open",self)
            open_actio.triggered.connect(lambda: list_Dclicked(history_list[self.window_index][here[self.window_index][0]][0], str(self.ui.listView.currentItem().text()),self.ui.listView,self.ui.lineEdit, self.window_index))
            self.menu.addAction(open_actio)

            if isdir( str(history_list[self.window_index][here[self.window_index][0]][0]) + "\\" + str(selected_item[0]) ) :
                open_innew_actio = QtGui.QAction("Open in new window",self)
                addressList = [history_list[self.window_index][here[self.window_index][0]][0]+str(self.ui.listView.currentItem().text()),
                               history_list[self.window_index][here[self.window_index][0]][0]]
                open_innew_actio.triggered.connect(lambda : newWindow(addressList))
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
            rename_actio.triggered.connect(self.rename)
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
        self.ui.actionSingUp.triggered.connect(lambda : self.User_("SingUp"))
        self.ui.actionLogin.triggered.connect(lambda : self.User("Login"))
        #self.ui.actionLogin.triggered.connect(self.User)
        #self.ui.actionLogin.triggered.connect(self.User)
        self.ui.actionPaste.triggered.connect(self.paste)
        self.ui.actionDelete.triggered.connect(self.delete)
        # self.ui.pushButton_3.clicked.connect(self.forward)
        self.ui.actionSetting.triggered.connect(self.Setting)
        self.ui.actionConnect.triggered.connect(self.Connect)
        self.User_l.SingButton.clicked.connect(self.send_result_)
        self.User_SU.SingButton.clicked.connect(self.send_result__)
        self.ui.pushButton_2.clicked.connect(lambda: history_back(self.ui, self.window_index))
        self.ui.pushButton_3.clicked.connect(lambda: history_forward(self.ui, self.window_index))
        self.ui.lineEdit_2.returnPressed.connect(lambda: self.search(self.ui.lineEdit_2.text()))
        self.Rename.RenameButton.clicked.connect(self.done_rename_)

    def selected_saver(self, item, selected_item_list=selected_item):
        """
        | This method saves text of selected item into the selected_item list
         selected_saver(self, item[, selected_item_lis  t=selected_item])
         :param item:Object
         :param selected_item_list:list
        """
        selected_item_list.pop()
        selected_item_list.append(str(item.text()))
        # print selected_item[0]
        # self.ui.lineEdit.setText(selected_item[0])

    def treeWidget_itemClicked(self, itemList, selected_item):
        self.ui.lineEdit.setText(self.ui.treeWidget.currentItem().dir)
        self.ui.listView.clear()
        add_here(self.ui.treeWidget.currentItem().dir, self.window_index)
        listView(self.ui.treeWidget.currentItem().dir, self.ui.listView)


    def up(self,h_list=history_list):
        try:
            this_dir = history_list[self.window_index][here[self.window_index][0]][0]
            list_dir = this_dir.split("\\")
            p_dir = ""
            for i in range(len(list_dir)-1):
                p_dir = p_dir + list_dir[i] + "\\"

            p_dir = p_dir[0:len(p_dir)-1]
            add_here(p_dir, self.window_index)
            self.ui.lineEdit.setText(p_dir)
            self.ui.listView.clear()
            listView(p_dir,self.ui.listView)
        except  IndexError :
            return False

    def start_show(self, app):
        self.show()
        if sys.exit(app.exec_()):
            if self.sub_proccess:
                self.sub_proccess.kill()

    def copy(self, action, item=selected_item):
        """
        | This method calls copy_action function for selected item
        :param action:QAction
        :param item:list
        """
        copy_action(item[0], history_list[self.window_index][here[self.window_index][0]][0])


    def cut(self, action, item=selected_item):
        """
        | This method calls cut_action function for selected item
        :param action:QAction
        :param item:list
        """
        cut_action(item[0], history_list[self.window_index][here[self.window_index][0]][0])

    def send_result_(self):
        print self.User_l.item_list , 123456
        if self.User_l.item_list[0] and self.User_l.item_list[1]:
            if not self.server_is_run:
                self.sub_proccess = Popen([sys.executable, 'Socket\\server.py'])
                self.server_is_run = True
            print 'opened'
            set_setting("user_name", self.User_l.item_list[0])
            send_result("0|" + self.User_l.item_list[0] + "|" + self.User_l.item_list[1])
            print 1

    def send_result__(self):
        print self.User_SU.item_list, 123456
        if self.User_SU.item_list[0] and self.User_SU.item_list[1]:
            if not self.server_is_run:
                self.sub_proccess = Popen([sys.executable, 'Socket\\server.py'])
                self.server_is_run = True
            set_setting("user_name", self.User_SU.item_list[0])
            local_server = get_setting_value('server_id')[0]
            local_port = get_setting_value('port_number')[0]
            # print local_server
            # print local_port
            send_result("1|" + self.User_SU.item_list[0] + "|" + self.User_SU.item_list[1] + "|" + local_server + "|" + local_port + "|" + "1")
            # print 0

    def paste(self, action):
        """
        | This function calls paste_action function for current directory. Before that it'll clear QListWidget
        :param action:QAction
        """
        self.ui.listView.clear()                    # This line clears QListWidget
        paste_action(history_list[self.window_index][here[self.window_index][0]][0], self.ui.listView)

    def delete(self, action, item=selected_item):
        self.ui.listView.clear()
        delete_action(item[0], history_list[self.window_index][here[self.window_index][0]][0], self.ui.listView)

    def rename(self):
        self.Rename.rename_()

    def done_rename_(self,action , item=selected_item):
        done_rename(item[0], history_list[self.window_index][here[self.window_index][0]][0] + '\\' +  item[0])

    def search(self, item):
        add_here(history_list[self.window_index][here[self.window_index][0]][0], self.window_index)
        if history_list[self.window_index][here[self.window_index][0]][0] != "*\\*":
            result = search(str(item), history_list[self.window_index][here[self.window_index][0]][0])
        else:
            result = search(str(item), history_list[self.window_index][here[self.window_index][0] - 1][0])
        # print "WHOLE result"
        # print result
        """
        if not result:
            result = step_by_step_search(str(item), history_list[here[0]][0])
        # print "kojoloo result"
        # print result
        """
        if result:
            self.ui.listView.clear()
            listView(result, self.ui.listView)
            add_here("*\\*", self.window_index,parent="*")
    def Setting(self):
        self.User_S._Setting_()
        # user_name = str(self.User_S.fileComboBox.text())
        # server_id = str()
        # port_num =
        # print "****"
        # print self.User_S.fileComboBox.text()
        # print server_id
        # print port_num
        self.User_S.SingButton.clicked.connect(lambda: self.add_setting_in_db(str(self.User_S.textComboBox.text()), str(self.User_S.text1ComboBox.text())))

    def add_setting_in_db(self, server, port):
        # print 'kir'
        # print server
        # print port
        # set_setting('user_name', user_name)
        set_setting('server_id', server)
        set_setting('port_number', port)


    def Connect(self):
        self.User_C._Setting_C()
        self.User_C.SingButton.clicked.connect(lambda: self.Make_sock_Win(str(self.User_C.fileComboBox.text())))

    def Make_sock_Win(self, provider_username):
        provider_username_list.append(provider_username)
        if not provider_username:
            # print 'inja'
            return
        if not self.server_is_run:
                Popen([sys.executable, 'Socket\\server.py'])
                self.server_is_run = True
        self.sockWin = SocketMainWindow()
        # print 'The UI'
        # print self.sockWin.window_index
        self.sockWin.show()
        #self.Us

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
        # print self.memory_list , file_name , current_directory , 1234
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
        # print self.memory_list , current_directory , 516165
        #memory_list[1] = ((memory_list[-1].split('\\'))[0])
        if self.memory_list:
            if not self.memory_list[0]:
                if isdir(self.memory_list[1]):
                    directory = Directory(self.memory_list[1])
                    directory.copy(current_directory)
                else:
                    file_object = File(self.memory_list[1])
                    file_object.copy(current_directory)

    def User(self , action):
        self.User_l._User(self ,action)

    def User_(self , action):
        self.User_SU._User_(self ,action)

def newWindow(addressList):
    newWin = MainWindow()
    history_list[newWin.window_index]=[addressList]
    newWin.ui.listView.clear()
    listView(history_list[newWin.window_index][0][0], newWin.ui.listView)
    newWin.show()

def updator():
    while True:
        sleep(0.5)
        # print 'kir'
        for window in winList:
            if history_list[window.window_index][here[window.window_index][0]][0]:
                newFileList = get_files(history_list[window.window_index][here[window.window_index][0]][0])
                newDirList = get_directories(history_list[window.window_index][here[window.window_index][0]][0])
                ctr = 0
                num = window.ui.listView.count()
                #print "ctr ", ctr, " num ", num
                while (ctr < num):
                    #print "ctr ", ctr, " num ", num
                    print ctr
                    if str(window.ui.listView.item(ctr).text()) not in newDirList + newFileList:
                        window.ui.listView.takeItem(ctr)
                        num -= 1
                    else:
                        ctr += 1
                oldList = []
                num = window.ui.listView.count()
                for intItr in range(num):
                    oldList.append(str(window.ui.listView.item(intItr).text()))
                for itr in newDirList:
                    if not (itr in oldList):
                        item = QtGui.QListWidgetItem()
                        item.setText(itr)
                        icon = QtGui.QIcon("icons\\folder.ico")
                        item.setIcon(icon)
                        window.ui.listView.addItem(item)
                for itr in newFileList:
                    if not (itr in oldList):
                        item = QtGui.QListWidgetItem()
                        item.setText(itr)
                        icon = QtGui.QIcon(file_icon(itr))
                        item.setIcon(icon)
                        window.ui.listView.addItem(item)

            else:
                newFileList = []
                newDirList =[]



if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    Win = MainWindow()
    upd = Thread(target=updator)
    upd.start()
    #newWindow(["D:\\ACM like", "D:\\"])
    Win.start_show(app)
