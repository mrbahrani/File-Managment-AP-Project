"""
This file is the Main Server file.
The rules of sending strings:
1. Each parts of requests must splits with | character without any white space before or after that.
2. Login request starts with 0 . The pattern is like : 0|user_name|password
3. SignUp request starts with 1. The pattern is like : 1|user_name|password|server_id|port number|ready_state
4. Changing state request starts with 2. The pattern hs like : 2|new_state|user_name
5. Getting file list from another user request starts with 3 .
    The pattern is like 3|userName|provider_username|directory path.
6. Search request starts with 4. The pattern is like : 4|userName|provider_username|word.
7. Copy request starts with 5.The pattern is like : 5|userName|provider_username|file_path|distance.
8. Cut request starts with 6.The pattern is like : 6|userName|provider_username|file_path|distance.
7. Delete request starts with 7.The pattern is like : 7|userName|provider_username|file_path.
7. Rename starts with 8.The pattern is like : 8|userName|provider_username|file_path|new name.
"""
import socket
from db import *
logged_in_users = []
socket_obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = str([l for l in ([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith("127.")][:1], [[(s.connect(('8.8.8.8', 80)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]]) if l][0][0])
port = 6985
socket_obj.bind((host, port))
socket_obj.listen(10)
while 1:
    client_socket, address = socket_obj.accept()
    request = client_socket.recv(1024)
    request_list = request.split("|")
    if not request_list[0]:
        is_valid = validate_user(request[1], request[2])
        if not is_valid:
            client_socket.sendall('0|')                           # If the user name or password is incorrect return 0|
            client_socket.close()
            break
        logged_in_users.append(request_list[1])                   # Added user name in logged_in_users list if is valid
    elif request_list[1] in logged_in_users:
        pass
