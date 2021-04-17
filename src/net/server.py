import socketserver
from signal import signal, SIGINT

MAX_SIZE = 1024

class Handler(socketserver.BaseRequestHandler):

    def handle(self):
        self.data = self.request.recv(MAX_SIZE).strip()
        print(self.data)

def setup(host, port):
    server = socketserver.TCPServer((host, port), Handler)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        server.server_close()
        exit(1)

def main():
    host = 'localhost'
    port = 5000
    setup(host, port)


if __name__ == "__main__":
    main()

