import socket
from events import *
from os.path import isdir, isfile
from os import listdir

file_list = ''
memory = []
memory_list = []
list = []
newpath = []


def connect():
    """
    | This function creates a connection to the 192.168.85.69 ip and 6985 port and then returns the connection object
    | If any exception throws, an error massage prints.
    """
    try:
        socket_obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host = '192.168.85.69'                              # Server Ip address
        port = 6985                                         # Server port number
        socket_obj.connect((host, port))
        return socket_obj
    except socket.error:
        print 'pander'


def close(connection_obj):
    """
    | This function gets a connection object and close that.
    :param connection_obj :Socket object
    """
    connection_obj.close()


def send_files_list(path):
    """
    | This function returns a string of all files and directories included in path directory.
    | All directories names start with '0' and all files names start with '1';
    | If the path is not a directory, returns '0|'
    :param path :str
    """
    if isdir(path):
        # Adds all directories names to the final_string variable
        final_string = "".join(['0' + element + "|" for element in listdir(path) if isdir(path + element)])
        # Adds all files names to the final_string variable
        final_string += "".join(['1' + element + "|" for element in listdir(path) if isfile(path + element)])
        return final_string
    return "0|"


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

