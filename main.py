import socket
import threading

soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soc.bind(('0.0.0.0', 8000))
soc.listen(1)
connections = []

def targetHandler(conn, client_add):
    global connections
    while True:
        data = conn.recv(1024)
        for item in connections:
            item.send(bytes(data))
        if not data:
            connections.remove(conn)
            conn.close()
            break



while True:
    connection, client_address = soc.accept() 
    thread = threading.Thread(target=targetHandler, args=(connection, client_address))
    thread.daemon = True
    thread.start()
    connections.append(connection)
    print(connections)
