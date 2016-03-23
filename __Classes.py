from os import rename, access, remove, R_OK, F_OK, startfile, listdir
from __ErrorHandler import error_show
from __exceptions import FileNotExist,NoPermission
from shutil import rmtree, copy2, copytree


class File(object):
    def __init__(self, strAdrs):
        self.fullPath = strAdrs
        self.__existence()
        self.__reachable()
        self.type = strAdrs.split(".")[-1]
        self.name = strAdrs.split("\\")[-1][:]
        # self.Jname = strAdrs.name.split(".")[0]
        self.Jname = strAdrs.split(".")[0]
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
        """
        This method opens the file.
        """
        try:
            startfile(self.fullPath)
        except Exception:
            print ("An exception ocurred during open")

    def copy(self, dest):
        """
        This method creates a copy of the file.
        parameters:
        self : Object
        dest : new file's address
        """
        try:
            print dest
            print self.fullPath
            copy2(self.fullPath, dest)
            self.fullPath = dest
        except Exception as e:
            print e
            print ("An exception ocurred during copy")

    def cut(self, second_path):
        """
        | This method moves a file from current directory to the second directory.
        :param self : Object
        :param second_path: str
        """
        try:
            rename(self.fullPath, second_path)
            self.delete()
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
            rename(self.fullPath, ''.join(self.fullPath.split('\\')[:len(self.fullPath) - len(self.type) - len(self.name)]) + new_name)
        except WindowsError:
            error_show('The second directory path is invalid', 'listener must add')
        except Exception:
            error_show("An Error happened, please restart the app.", 'listener must add')


class Directory(object):
    def __init__(self, strAdrs):
        self.fullAddress = strAdrs
        self.name = strAdrs.split("\\")[-1]
        try:
            if strAdrs.split("\\")[-1]:
                self.parent = strAdrs.split("\\")[-2]
            else:
                self.parent = None
        except IndexError:
            self.parent = None
        self.children = list()

    def openf(self):
        file_list = []
        for filename in listdir(self.fullAddress):
            file_list.append(filename)
        return file_list
        
    def copy(self, dest):
        copytree(self.fullAddress, dest)

    def cut(self, dest):
        self.copy(self, dest)
        self.delete()

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
            rename(self.fullAddress, ''.join(self.fullAddress[:len(self.fullAddress) - len(self.name)]) + new_name)
        except WindowsError:
            error_show('The second directory path is invalid', 'listener must add')
        except Exception:
            error_show("An Error happened, please restart the app.", 'listener must add')
