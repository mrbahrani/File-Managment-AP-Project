import socket
import sys
# import os.path
# sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from Socket.Client import *
from Socket.db import *
import socket
from Socket.funcssock import *

#last_request_directory_list = []
#last_request_directory_string_list=[]
socket_obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = get_setting_value('server_id')                                   # Gets server ip from data base
port = get_setting_value('port_number')                                 # Gets server port from data base
# port = 8585
print host
print socket
socket_obj.bind((host[0], int(port[0])))
socket_obj.listen(1)
my_username = get_setting_value('user_name')


while 1:
    main_server, address = socket_obj.accept()
    request = main_server.recv(1024)
    print request
    request_list = request.split("|")
    request_type = request_list[0]
    if request_type == '3':                         # Send files list request scope
        result = send_files_list(request_list[-1])
        send_result('9|' + my_username + "|" + request_list[2] + "|" + result)
        main_server.close()
        break
    elif request_type == '4':                       # search request scope
        result = client_search(request_list[3], request_list[4])
        send_result('10|' + request_list[1] + "|" + request_list[2] + "|" + result)
        main_server.close()
        break
    elif request_type == '5':                       # Copy request scope
        result = client_copy_file(request_list[3], request_list[4])
        send_result('11|' + request_list[1] + "|" + request_list[2] + "|" + request)
        main_server.close()
        break
    elif request_type == '6':                       # Cut request scope
        result = client_cut_file(request_list[3], request_list[4])
        send_result('12|' + request_list[1] + "|" + request_list[2] + "|" + request)
        main_server.close()
        break
    elif request_type == '7':                       # delete request scope
        result = delete_file(request_list[3], request_list[4])
        send_result('13|' + request_list[1] + "|" + request_list[2] + "|" + request)
        main_server.close()
        break
    elif request_type == '8':                       # Rename request scope
        pass
    elif request_type == '9':                       # Get file request scope
        print request_list[-1]
        last_request_directory_list.append(dir_file_list(request_list[-1]))
        last_request_directory_string_list.append(request_list[-1])
        #clientListView(request_list[-1] ,Sockapp)


    elif request_type == '10':                      # Get search result scope
        pass
    elif request_type == '11':                      # Get Copy result scope
        pass
    elif request_type == '12':                      # Get Cut result scope
        pass
    elif request_type == '13':                      # Get delete result scope
        pass
    else:
        main_server.sendall('0|')                           # If the request is not valid 0|
        main_server.close()
        break
print 'tamom'