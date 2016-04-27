"""
This file is the Main Server file.
The rules of sending strings:
1. Each parts of requests must splits with | character without any white space before or after that.
2. Login request starts with 0 . The pattern is like : 0|user_name|password
3. SignUp request starts with 1. The pattern is like : 1|user_name|password|server_id|port number|ready_state
4. Changing state request starts with 2. The pattern hs like : 2|user_name|new_state
5. Getting file list from another user request starts with 3 .
    The pattern is like 3|userName|provider_username|directory path.
6. Search request starts with 4. The pattern is like : 4|userName|provider_username|path|word.
7. Copy request starts with 5.The pattern is like : 5|userName|provider_username|file_path|destination.
8. Cut request starts with 6.The pattern is like : 6|userName|provider_username|file_path|destination.
9. Delete request starts with 7.The pattern is like : 7|userName|provider_username|file_path|file_name.
10. Rename starts with 8.The pattern is like : 8|userName|provider_username|file_path|new name.
11. get file request starts with 9. the pattern is like : 9|userName|Provider_username|file_path
12. get search result starts with 10. The pattern is like : 10|userName|Provider_username|result_string
13. Get Copy result starts with 11. The pattern is like : 11|userName|provider_username|result_string
14. Get Cut result starts with 12. The pattern is like : 12|userName|provider_username|result_string
15. Get Delete result starts with 13. The pattern is like : 13|userName|provider_username|result_string
"""
import socket
from db import *
logged_in_users = []
# print socket.gethostname()
socket_obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 6985
# try:
socket_obj.bind((host, port))
socket_obj.listen(10)
create_users_table()
while True:
    client_socket, address = socket_obj.accept()
    request = client_socket.recv(1024)
    request_list = request.split("|")
    request_type = request_list[0]
    print request, request_list, request_type
    if request_type == '0':
        is_valid = validate_user(request_list[1], request_list[2])
        if not is_valid:
            print 'not logged in'
            print request_list
            client_socket.sendall('0|')                           # If the user name or password is incorrect return 0|
            client_socket.close()
            continue
        logged_in_users.append(request_list[1])                   # Added user name in logged_in_users list if is valid
        print 'logged in'
        client_socket.close()
    elif request_type == '1':
        add_new_user(request_list[1], request_list[2], request_list[3], request_list[4], request_list[5])
        print 'user added'
        client_socket.close()
        continue
    elif request_list[1] in logged_in_users:
        if request_type == '2':
            change_ready_state(request_list[1], request_list[2])
            client_socket.close()
            continue
        elif request_list[2] not in logged_in_users:
            client_socket.sendall('0|')                           # If the user name or password is incorrect return 0|
            client_socket.close()
            continue
        elif request_type in ['3', '4', '5', '6', '7', '8']:
            request_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            print 'kiri'
            print order(request_list[2])
            order_result = order(request_list[2])[0]
            request_server = order_result[0]
            request_port = order_result[1]
            print "IN TEH MAIN SERVER"
            print request_server
            print request_port
            print request
            request_socket.connect((request_server, int(request_port)))
            request_socket.sendall(request)
            request_socket.close()
            client_socket.close()
            continue
        elif request_type in ['9', '10', '11', '12', '13']:
            print 'send request'
            print request
            request_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            request_server, request_port = order(request_list[1])
            request_socket.connect((request_server, request_port))
            request_socket.sendall(request)
            request_socket.close()
            client_socket.close()
            continue
    else:
        client_socket.sendall('0|')                           # If the user name or password is incorrect return 0|
        client_socket.close()
        continue
# except socket.error:
#     print 'problem'
# finally:
socket_obj.close()
