from os import rename, access, remove, R_OK, F_OK
from ErrorHandler import error_show
from exceptions import FileNotExist, NoPermission
from shutil import rmtree


class File(object):
    def __init__(self, strAdrs):
        self.fullPath = strAdrs
        self.__existence()
        self.__reachable()
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

    def __reachable(self):
        if not access(self.fullPath, R_OK):
            raise NoPermission

    def openf(self):
        pass
        
    def copy(self,dest):
        pass

    def cut(self, second_path):
        """
        | This method moves a file from current directory to the second directory.
        :param self : Object
        :param second_path: str
        """
        try:
            rename(self.fullPath, second_path)
        except WindowsError:
            error_show('The second directory path is invalid', 'listener must add')
        except Exception:
            error_show("An Error happened, please restart the app.", 'listener must add')

    def delete(self):
        """
        | This method deletes current file.
        :param self: Obj
        """
        try:
            remove(self.fullPath)
        except WindowsError:
            error_show('The path is invalid', 'listener must add')
        except Exception:
            error_show("An Error happened, please restart the app.", 'listener must add')

    def rename(self, new_name):
        """
        | This method renames current file
        :param self: Obj
        :param new_name:str
        """
        try:
            rename(self.fullPath, ''.join(self.fullPath[:len(self.fullPath) - 1]) + new_name)
        except WindowsError:
            error_show('The second directory path is invalid', 'listener must add')
        except Exception:
            error_show("An Error happened, please restart the app.", 'listener must add')


class Directory(object):
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
        """
        | This method deletes current directory and all it's contents.
        :param self: Obj
        """
        try:
            rmtree(self.fullAddress)
        except WindowsError:
            error_show('The path is invalid', 'listener must add')
        except Exception:
            error_show("An Error happened, please restart the app.", 'listener must add')

    def rename(self, new_name):
        """
        | This method renames current directory
        :param self: Obj
        :param new_name:str
        """
        try:
            rename(self.fullAddress, ''.join(self.fullAddress[:len(self.fullAddress) - 1]) + new_name)
        except WindowsError:
            error_show('The second directory path is invalid', 'listener must add')
        except Exception:
            error_show("An Error happened, please restart the app.", 'listener must add')