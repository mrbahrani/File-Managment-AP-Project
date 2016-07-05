import socket
import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from search import search
from funcs import drivers
from events import copy_action, cut_action, paste_action, delete_action
from os.path import isdir, isfile
from os import listdir
from db import get_setting_value, create_settings_table

file_list = ''
memory = []
memory_list = []
list = []
newpath = []
create_settings_table()


def connect():
    """
    | This function creates a connection to the 192.168.85.69 ip and 6985 port and then returns the connection object
    | If any exception throws, an error massage prints.
    """
    # try:
    socket_obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    database_server_ip = get_setting_value('main_server_ip')
    database_server_port = get_setting_value('main_server_port')
    print "%%%%%%%%%%"
    print database_server_port
    print database_server_ip
    database_server_port = 6985
    database_server_ip = '169.254.17.121'
    if not database_server_ip:
        host = '127.0.0.1'                              # Server Ip address
    else:
        host = database_server_ip
    if not database_server_port:
        port = 6985                                         # Server port number
    else:
        port = database_server_port
    socket_obj.connect(("Mohammadreza", 6985))
    return socket_obj
    # except socket.error:
    #     print 'pander'


def close_connection(connection_obj):
    """
    | This function gets a connection object and close that.
    :param connection_obj :Socket object
    """
    connection_obj.close()


def send_files_list(path_str):
    """
    | This function returns a string of all files and directories included in path directory.
    | All directories names start with '0' and all files names start with '1';
    | If the path is not a directory, returns '0|'
    :param path :str
    """
    if isdir(path_str):
        # Adds all directories names to the final_string variable
        final_string = "".join(['0' + element + "|" for element in listdir(path_str) if isdir(path_str + element)])
        # Adds all files names to the final_string variable
        final_string += "".join(['1' + element + "|" for element in listdir(path_str) if isfile(path_str + element)])
        return final_string
    elif not path_str:
        final_string = "".join(['0' + element + "|" for element in drivers()])
    return "0|"

def client_copy_file(start_path, destination_path):
    """
    | This function copies a file or directory from start_path to the destination_path and finally returns
    |destination_path's files and directions with send_files_list function help.
    :param start_path : str
    :param destination_path :str
    :return str
    """
    file_path_list = start_path.split('\\')
    file_path = "".join(file_path_list[:len(file_path_list)])
    copy_action(file_path_list[-1], file_path)
    paste_action(destination_path, None)
    return send_files_list(destination_path)


def client_cut_file(start_path, destination_path):
    """
    | This function cuts a file or directory from start_path to the destination_path and finally returns
    |destination_path's files and directions with send_files_list function help.
    :param start_path : str
    :param destination_path :str
    :return str
    """
    file_path_list = start_path.split('\\')
    file_path = "".join(file_path_list[:len(file_path_list)])
    cut_action(file_path_list[-1], file_path)
    paste_action(destination_path, None)
    return send_files_list(destination_path)


def delete_file(element, element_path):
    """
    | This function deletes an element from element path and finally returns element_path's files and directions with
    | send_files_list function help.
    :param element :str
    :param element_path :str
    :return str
    """
    delete_action(element, element_path, None)
    return send_files_list(element_path)


def client_search(path_str, word):
    """
    | This function searching the path_str with search function and returns result as a string.
    | All directories names start with '0' and all files names start with '1'
    :param path_str :str
    :param word :str
    :return str
    """
    search_result = search(word, path_str)
    # Adds all directories names to the final_string variable
    final_string = "".join(['0' + element + "|" for element in search_result if isdir(element)])
    # Adds all files names to the final_string variable
    final_string += "".join(['1' + element + "|" for element in search_result if isfile(element)])
    return final_string


def send_result(result_string):
    """
    | This function sends result_string to the MainServer
    :param result_string str
    """
    connection_obj = connect()
    connection_obj.sendall(result_string)
    print connection_obj.recv(1021)
    close_connection(connection_obj)


def file_list_request(username,provider_username,directory):

    send_result("3|"+username+"|"+provider_username+"|"+directory)


def search_request(username, provider_username,path,word):
    send_result("4|"+username+"|"+provider_username+"|"+path+"|"+word )


def copy_request(username,provider_username,file_path,destination):
    send_result("5|"+username+"|"+provider_username+"|"+file_path+"|"+destination )


def cut_request(username,provider_username,file_path,destination):
    send_result("6|"+username+"|"+provider_username+"|"+file_path+"|"+destination )


def delete_request(username,provider_username,file_path,file_name):
    send_result("7|"+username+"|"+provider_username+"|"+file_path+"|"+file_name )


def rename_request(username,provider_username,file_path,new_name):
    send_result("8|"+username+"|"+provider_username+"|"+file_path+"|"+new_name )


