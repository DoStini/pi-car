import socketserver
import socket
from signal import signal, SIGINT

from picar.config import config
from picar.controller import handle_data

MAX_SIZE = 1024

def get_local_address():
    return [l for l in ([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] 
            if not ip.startswith("127.")][:1], [[(s.connect(('8.8.8.8', 53)), 
            s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, 
            socket.SOCK_DGRAM)]][0][1]]) if l][0][0]

class Handler(socketserver.BaseRequestHandler):
    def handle(self):
        self.data = self.request.recv(MAX_SIZE).strip()
        print(self.data)
        handle_data.toggle()

def setup(host, port):
    server = socketserver.TCPServer((host, port), Handler)
    print(f'Server at HOST[{host}], PORT[{port}] is now open')
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        server.server_close()
        print(f'Server at HOST[{host}], PORT[{port}] is now closed')
        exit(1)

def main():
    cfg = config.get_config()
    host = get_local_address()
    port = cfg["PORT"]
    print(host, port)
    setup(host, port)


if __name__ == "__main__":
    main()

