import socket
import sys
from time import sleep

MAX_SIZE = 1024
MAX_CONN_TRIES = 2
CONN_INTERVAL_SLEEP = 2

class ClosedServer(Exception):
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def __str__(self):
        return f'Server at HOST[{self.host}], PORT[{self.port}] is closed'

def setup(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    for x in range(MAX_CONN_TRIES):
        try:
            sock.connect((host, port))
        except:
            sleep(CONN_INTERVAL_SLEEP)
            continue
        return sock
    raise ClosedServer(host, port)

def send_data(sock, data):
    sock.sendall(bytes(data + "\n", "utf-8"))

def main():
    host = 'localhost'
    port = 5000
    try: 
        sock = setup(host, port)
    except ClosedServer as err:
        print(err)
        exit(2)
    
    send_data(sock, "hello world")
    sock.close()


if __name__ == "__main__":
    main()

