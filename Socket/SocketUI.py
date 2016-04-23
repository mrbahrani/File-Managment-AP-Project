from DefaultUI import *
from app import *

class SocketMainWindow(QtGui.QSocketMainWindow, New_File, New_Dir,User_D,User_S):
    index = 0

    def __init__(self):
        super(SocketMainWindow, self).__init__()
        self.setWindowIcon(QtGui.QIcon('icons\\mycomputer.ico'))
        self.window_index = SocketMainWindow.index
        SocketMainWindow.increase_index()
        self.prepare_lists()
        self.New_File = New_File()
        self.ui = Ui_MainWindow()
        self.New_File = New_File()
        print history_list[self.window_index][here[self.window_index][0]][0]
        self.New_Dir = New_Dir()
        self.Rename = Rename_()
        self.User_D = User_D()
        self.User_S = User_S()
        self.User_C = User_C()
        self.ui.setupUi(self)
        self.add_actions()
        self.setup()
        self.memory_list = []
        self.list = []
        self.list_ = []
        lLock.append(Lock())

        self.dragOver = False
        
        self.setAcceptDrops(True)
        self.ui.listView.setDragEnabled(True)
        self.ui.listView.setDragDropMode(QtGui.QAbstractItemView.InternalMove)

    @staticmethod
    def increase_index():
        SocketMainWindow.index += 1

    def prepare_lists(self):
        here.append([0])
        history_list.append([["", ""]])

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
        super(SocketMainWindow, self).dragMoveEvent(event)

    def dropEvent(self, event):
        self.list = list()
        self.list_ = list()
        self.memory_list = []
        if event.mimeData().hasUrls():
            print event.mimeData().urls()
            for url in event.mimeData().urls():
                self.list.append(str(url.path()))
            event.acceptProposedAction()
            self.list_ = self.list[0].split('/')
            # print self.list_ ,self.list
                                                                                     
            self.copy_action_(self.list_[-1], (self.list[0])[2:])

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

            treeView(driver, tree_widget_item,self.window_index)
        for driver in drivers():
            list_widget_item = QtGui.QListWidgetItem(self.ui.listView)
            list_widget_item.setIcon(QtGui.QIcon('icons\\mycomputer.ico'))
            list_widget_item.setText(driver)
        self.ui.treeWidget.itemClicked.connect(self.treeWidget_itemClicked)
        self.ui.listView.itemClicked.connect(self.selected_saver)
        self.ui.treeWidget.itemExpanded.connect(lambda item:treeWidget_itemExpanded(item,self.window_index) )
        if history_list[self.window_index][here[self.window_index][0]][0] != "*":
            self.ui.listView.doubleClicked.connect(lambda: list_Dclicked(history_list[self.window_index][here[self.window_index][0]][0], str(self.ui.listView.currentItem().text()),self.ui.listView,self.ui.lineEdit, self.window_index))
        self.ui.listView.itemClicked.connect(self.selected_saver)

        self.ui.pushButton.clicked.connect(self.up)

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Return:
            if self.ui.listView.currentItem():
                list_Dclicked(history_list[self.window_index][here[self.window_index][0]][0], str(self.ui.listView.currentItem().text()), self.ui.listView, self.ui.lineEdit, self.window_index)

    def contextMenuEvent(self , event):
        # print selected_item
        self.menu = QtGui.QMenu(self)
        if selected_item[0] != "" :
            open_actio = QtGui.QAction("Open", self)
            open_actio.triggered.connect(lambda: list_Dclicked(history_list[self.window_index][here[self.window_index][0]][0], str(self.ui.listView.currentItem().text()),self.ui.listView,self.ui.lineEdit, self.window_index))
            self.menu.addAction(open_actio)

            if isdir(str(history_list[self.window_index][here[self.window_index][0]][0]) + "\\" + str(selected_item[0]) ) :
                open_innew_actio = QtGui.QAction("Open in new window",self)
                open_innew_actio.triggered.connect(lambda: newWindow(self))
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
        self.ui.actionSingUp.triggered.connect(lambda : self.User("SingUp"))
        self.ui.actionLogin.triggered.connect(lambda : self.User("Login"))
        #self.ui.actionLogin.triggered.connect(self.User)
        #self.ui.actionLogin.triggered.connect(self.User)
        self.ui.actionPaste.triggered.connect(self.paste)
        self.ui.actionDelete.triggered.connect(self.delete)
        #self.ui.actionRename.triggered.connect(self.rename)
        self.ui.actionSetting.triggered.connect(self.Setting)
        self.ui.actionConnect.triggered.connect(self.Connect)
        # self.ui.pushButton_3.clicked.connect(self.forward)
        self.User_D.SingButton.clicked.connect(self.send_result_)
        self.ui.pushButton_2.clicked.connect(lambda: history_back(self.ui, self.window_index))
        self.ui.pushButton_3.clicked.connect(lambda: history_forward(self.ui, self.window_index))
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
            for i in range(len(list_dir)-2):
                p_dir = p_dir + list_dir[i] + "\\"
            add_here(p_dir, self.window_index)
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
        copy_action(item[0], history_list[self.window_index][here[self.window_index][0]][0])
        
    def send_result_(self):
        print self.User_D.item_list , 123456
        if self.User_D.item_list[0] and self.User_D.item_list[1]:
            send_result("0|" + self.User_D.item_list[0] + "|" + self.User_D.item_list[1])
            print 1
    def cut(self, action, item=selected_item):
        """
        | This method calls cut_action function for selected item
        :param action:QAction
        :param item:list
        """
        cut_action(item[0], history_list[self.window_index][here[self.window_index][0]][0])

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

    def rename(self ):
        self.Rename.rename_()

    def search(self, item):
        print "SEARCH"
        add_here(history_list[self.window_index][here[self.window_index][0]][0], self.window_index)
        if history_list[self.window_index][here[self.window_index][0]][0] != "*\\*":
            result = search(str(item), history_list[self.window_index][here[self.window_index][0]][0])
        else:
            result = search(str(item), history_list[self.window_index][here[self.window_index][0] - 1][0])
        print result
        if result:
            self.ui.listView.clear()
            listView(result, self.ui.listView)
            add_here("*\\*", self.window_index)


    def Setting(self):
        self.User_S._Setting_()


    def Connect(self):
        self.User_C._Setting_C()


    def NewDir(self):
        print "#######"
        print history_list[self.window_index][here[self.window_index][0]][0]
        self.New_Dir._NewDir()

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
        # prin1t "PASTE"
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
        self.User_D._User(self,action)


class Updator(QtCore.QThread):
    def __init__(self, winList):
        super(Updator,self).__init__()
        self.winList = winList

    def run(self):
        oldList = []
        newListF= []
        newListD= []
        while True:
            sleep(0.05)
            for window in self.winList[1:2]:
                #print history_list[window.window_index],"WIN",window.window_index
                if history_list[window.window_index][here[window.window_index][0]][0] == "*\\*":
                    continue
                lLock[window.window_index].acquire()
                if history_list[window.window_index][here[window.window_index][0]][0] == "":
                    newListD = []
                    newListF = []
                else:
                    newListD = get_directories(history_list[window.window_index][here[window.window_index][0]][0])
                    newListF = get_files(history_list[window.window_index][here[window.window_index][0]][0])
                ctr = window.ui.listView.count()
                for itr in range(ctr):
                    try:
                        oldList += [str(window.ui.listView.item(itr).text())]
                    except UnicodeEncodeError as e:
                        print "UNICODE ERROR"
            # *********************************
                if newListF is None:
                    return
                for itrF in newListF:
                    if not (itrF in oldList):
                        item = QtGui.QListWidgetItem()
                        item.setText(itrF)
                        icon = QtGui.QIcon(file_icon(itrF))
                        item.setIcon(icon)
                        window.ui.listView.addItem(item)
                for itrD in newListD:
                    if not (itrD in oldList):
                        item = QtGui.QListWidgetItem()
                        item.setText(itrD)
                        icon = QtGui.QIcon("icons\\folder.ico")
                        item.setIcon(icon)
                        window.ui.listView.addItem(item)
            # *********************************
                if history_list[window.window_index][here[window.window_index][0]][0]=="":
                    newListD = drivers()
                    newListF = []
                else:
                    newListD = get_directories(history_list[window.window_index][here[window.window_index][0]][0])
                    newListF = get_files(history_list[window.window_index][here[window.window_index][0]][0])

                ommitList = []

                for itr in oldList:
                    if not (itr in newListD+newListF):
                        ommitList += [itr]
                num_of_items = window.ui.listView.count()
                holder = 0
                while holder <num_of_items:
                    if window.ui.listView.item(holder):
                        if str(window.ui.listView.item(holder).text()) in ommitList:
                            window.ui.listView.takeItem(holder)
                            num_of_items -=1
                        else:
                            holder +=1
            # *********************************
                oldList = []
                lLock[window.window_index].release()

def newWindow(pwin):
    #newApp = QtGui.QApplication()
    newWin = SocketMainWindow()
    windowList.append(newWin)
    dir = history_list[pwin.window_index][here[pwin.window_index][0]][0]+str(pwin.ui.listView.currentItem().text())
    history_list[newWin.window_index][0] = [dir,str(pwin.ui.listView.currentItem().text())]
    print history_list[newWin.window_index]
    #here[newWin.window_index] =[1]
        #history_list[pwin.window_index][here[pwin.window_index][0]]
    lLock[newWin.window_index+1].acquire()
    newWin.ui.listView.clear()
    #history_list[newWin.window_index][here[newWin.window_index][0]][0] = history_list[pwin.window_index][here[pwin.window_index][0]][0]
    #add_here(str(history_list[pwin.window_index][here[pwin.window_index][0]][0]),newWin.window_index)
    #list_Dclicked(history_list[newWin.window_index][here[newWin.window_index][0]][0], str(pwin.ui.listView.currentItem().text())
    #              ,newWin.ui.listView,newWin.ui.lineEdit, newWin.window_index)
    listView(history_list[newWin.window_index][0][0],newWin.ui.listView)
    newWin.show()
    #neU = Updator(newWin)
    #neU.start()
    lLock[newWin.window_index+1].release()


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    Win = SocketMainWindow()
    windowList.append(Win)
    updator = Updator(windowList)
    updator.start()
    Win.start_show(app)
    updator.terminate()