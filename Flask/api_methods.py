import socket
from app import *

def hello():
    res = {}
    sock = socket.socket()
    sock.bind(('', 9090))
    sock.listen(1)
    conn, addr = sock.accept()

    res["Hello"] = conn.recv(1024)
    conn.close()

    return res
