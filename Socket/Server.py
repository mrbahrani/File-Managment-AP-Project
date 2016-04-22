import socket
from Client import *
from db import *
import socket
socket_obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = get_setting_value('server_ip')                                   # Gets server ip from data base
port = get_setting_value('server_port')                                 # Gets server port from data base
socket_obj.bind((host, port))
socket_obj.listen(1)
my_username = get_setting_value('user_name')
while 1:
    main_server, address = socket_obj.accept()
    request = main_server.recv(1024)
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
    