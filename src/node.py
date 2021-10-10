import threading
import socket

class decentralize:
    def __init__(self, host, port):

        # Network Variables
        self.host = host
        self.port = port

        self.clients = []
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.bind((host, port))

    def handle(self, conn, addr):
        print(f"[NEW NODE] : {addr}")

        complete_info = ''
        connected = True
        while connected:
            msg = self.s.recv(7)
            if len(msg) <= 0:
                break
            complete_info += msg.decode("utf-8")

    def start_node(self):
        self.s.listen()
        while 1:
            conn, addr = self.s.accept()
            thread = threading.Thread(target=self.handle, args=(conn, addr))
            thread.start()
            print(f"ACTIVE CONNECTIONS: {threading.activeCount() - 1}")

    def connectToNode(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as k:
            k.connect((self.host, self.port))
            k.sendall(b'Hello, world')

            complete_info = ''
            connected = True
            while connected:
                data = self.s.recv(7)
                if len(data) <= 0:
                    break
                complete_info += data.decode("utf-8")
            print('Received', repr(data))
