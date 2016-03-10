from os import rename, access, R_OK, F_OK
from ErrorHandler import error_show
from exceptions import FileNotExist


class File(object):
    def __init__(self, strAdrs):
        self.fullPath = strAdrs
        self.type = strAdrs.split(".")[-1]
        self.name = strAdrs.split("\\")[-1]
        self.Jname = strAdrs.name.split(".")[0]
        self.parent = strAdrs.split("\\")[-2]

    def __existence(self):
        """
        | If the file has not exist , This private method raise a FileNotExist exception
        :param self : Object
        """
        if not access(self.fullPath, F_OK):
            raise FileNotExist

    def openf(self):
        pass
        
    def copy(self,dest):
        pass

    def cut(self, second_path):
        """
        | This method moves a file from current directory to the second directory.
        | If the file has not exist, a FileNotExist exception raise and handle.
        | If the second path has not exist, WindowsError exception will handle.
        :param self : Object
        :param second_path: str
        """
        try:
            self.__existence()
            rename(self.fullPath, second_path)
        except WindowsError:
            error_show('The second directory path is invalid', 'listener must add')
        except FileNotExist as error:
            error_show(str(error), 'listener must add')
        except Exception:
            error_show("An Error happened, please restart the app.", 'listener must add')

    def delete(self):
        pass

    def rename(self,newName):
        pass


class directory(object):
    def __init__(self, strAdrs):
        self.fullAddress = strAdrs
        self.name = strAdrs.split("\\")[-1]
        self.parent = strAdrs.split("\\")[-2]
        self.children = list()

    def openf(self):
        pass
        
    def copy(self,dest):
        pass

    def cut(self,dest):
        pass

    def delete(self):
        pass

    def rename(self, newName):
        pass
