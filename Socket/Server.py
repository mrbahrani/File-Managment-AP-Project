import socket
from Client import *
from MainServer.server import *

def connection():
    try:
        socket_obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host = '192.168.85.69'
        port = 6985
        socket_obj.bind((host),(port))
        socket_obj.listen(10)
        return socket_obj
    except socket.error:
        print 'pander'