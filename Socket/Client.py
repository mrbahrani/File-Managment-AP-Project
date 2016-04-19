import socket
from events import *
from MainServer.server import *
from app import *
from visual import *

file_list = ''
memory = []
memory_list = []
list = []
newpath = []
main_ = MainWindow()


def connect():
    try:
        socket_obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host = '192.168.85.69'
        port = 6985
        socket_obj.connect((host, port))
        return socket_obj
    except socket.error:
        print 'pander'


def close(connection_obj):
    connection_obj.close()


def send_file_list(path):
    file_list = list(path)
    newpath = listView(path, None)


    return True


def see_file(main):
    if True:
        main_

    return True


def copy_file(path):
    path_list = path.split("\\")
    current_directory = "".join(path_list[:len(path_list)])
    file_name = path_list[-1]
    copy_action(file_name, current_directory, list)

    return True


def cut_file(path):
    path_list = path.split("\\")
    current_directory = "".join(path_list[:len(path_list)])
    file_name = path_list[-1][7]
    cut_action(file_name, current_directory, list)

    return True


def paste(path, list):
    if list[0]:
        paste_action(request[5], None, list)
    else:
        paste_action(request[6], None, list)

    return True

def delete_file(path):
    path_list = path.split("\\")
    current_directory = "".join(path_list[:len(path_list)])
    if request[7]:
        delete_action(path, current_directory, None)
    return True


def rename_file(path):
    pass


def new_file(path):
    pass


def new_directory(path):
    pass


def response(conection, request_type):
    while True: pass

