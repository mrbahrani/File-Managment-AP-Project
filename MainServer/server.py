"""
This file is the Main Server file.
The rules of sending strings:
1. Each parts of requests must splits with | character without any white space before or after that.
2. Login request starts with 0 . The pattern is like : 0|user_name|password
3. SignUp request starts with 1. The pattern is like : 1|user_name|password|server_id|port number|ready_state
4. Changing state request starts with 2. The pattern hs like : 2|user_name|new_state
5. Getting file list from another user request starts with 3 .
    The pattern is like 3|userName|provider_username|directory path.
6. Search request starts with 4. The pattern is like : 4|userName|provider_username|word.
7. Copy request starts with 5.The pattern is like : 5|userName|provider_username|file_path|distance.
8. Cut request starts with 6.The pattern is like : 6|userName|provider_username|file_path|distance.
9. Delete request starts with 7.The pattern is like : 7|userName|provider_username|file_path.
10. Rename starts with 8.The pattern is like : 8|userName|provider_username|file_path|new name.
11 . get file request starts with 9. the pattern is like : 9|userName|Provider_username|file_path
"""
import socket
from db import *
logged_in_users = []
# print socket.gethostname()
socket_obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 6985
socket_obj.bind((host, port))
socket_obj.listen(10)
while True:
    print 1
    client_socket, address = socket_obj.accept()
    request = client_socket.recv(1024)
    request_list = request.split("|")
    request_type = request_list[0]
    print request, request_list, request_type
    if not request_type:
        is_valid = validate_user(request[1], request[2])
        if not is_valid:
            client_socket.sendall('0|')                           # If the user name or password is incorrect return 0|
            client_socket.close()
            break
        logged_in_users.append(request_list[1])                   # Added user name in logged_in_users list if is valid
    elif request_list[1] in logged_in_users:
        if request_type == '4':
            change_ready_state(request_list[1], request_list[2])
        elif request_list[2] not in logged_in_users:
            client_socket.sendall('0|')                           # If the user name or password is incorrect return 0|
            client_socket.close()
            break
        elif request_type == '5':
            pass

    elif request_type == '1':
        add_new_user(request_list[1], request_list[2], request_list[3], int(request_list[4]), int(request_list[5]))
    else:
        client_socket.sendall('0|')                           # If the user name or password is incorrect return 0|
        client_socket.close()
        break