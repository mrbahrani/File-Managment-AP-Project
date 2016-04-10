"""
This file is the Main Server file
"""
import socket
from db import *
socket_obj = socket(socket.AF_INET, socket.SOCK_STREAM)
host = str([l for l in ([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith("127.")][:1], [[(s.connect(('8.8.8.8', 80)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]]) if l][0][0])
port = 6985
socket_obj.bind((host, port))
socket_obj.listen(10)
while 1:
    client_socket, address = socket_obj.accept()
    client_info = client_socket.recv(1024)
    is_valid = validate_user(client_info[0], client_info[1])
    if is_valid:
        pass
