class File(object):
    def __init__(self,strAdrs):
        self.fullAddress = strAdrs
        self.type = strAdrs.split(".")[-1]
        self.name = strAdrs.split("\\")[-1]
        self.Jname = strAdrs.name.split(".")[0]
        self.parent = strAdrs.split("\\")[-2]
        
    def openf(self):
        pass
        
    def copy(self,dest):
        pass

    def cut(self,dest):
        pass

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
