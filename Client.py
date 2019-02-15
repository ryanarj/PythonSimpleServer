import socket
import threading

class Client:

    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connections = []
    def __init__(self):
        self.soc.connect()
        self.soc.listen(1)

    def targetHandler(self, conn, client_add):
        while True:
            data = conn.recv(1024)
            for item in self.connections:
                item.send(bytes(data))
            if not data:
                break


    def start(self):
        while True:
            connection, client_address = self.soc.accept() 
            thread = threading.Thread(target=self.targetHandler, args=(connection, client_address))
            thread.daemon = True
            thread.start()
            self.connections.append(connection)
            print(self.connections)

ServerSocket().start()
