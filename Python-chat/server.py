from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import time

def get_connections():
    while True:
        time.sleep(0.3)
        client, client_address = SERVER.accept()
        print("%s:%s connected." % client_address)
        client.send(bytes("Insert your nickname and press enter to start chatting.", "utf8"))
        addresses[client] = client_address
        Thread(target=client_processing, args=(client,)).start()

def client_processing(client):  
    name = client.recv(SIZE).decode("utf8")
    welcome = 'Welcome %s!' % name
    client.send(bytes(welcome, "utf8"))
    msg = "%s has joined!" % name
    send_all(bytes(msg, "utf8"))
    clients[client] = name

    while True:
        time.sleep(0.3)
        msg = client.recv(SIZE)
        if msg != bytes("$closeconnection", "utf8"):
            send_all(msg, name+": ")
        else:
            client.send(bytes("$closeconnection", "utf8"))
            client.close()
            del clients[client]
            send_all(bytes("%s has left the building!" % name, "utf8"))
            break


def send_all(msg, prefix=""): 
    for sock in clients:
        sock.send(bytes(prefix, "utf8")+msg)

        
clients = {}
addresses = {}

HOST = 'localhost'
PORT = 6666
SIZE = 4096
ADDRESS = (HOST, PORT)

SERVER = socket(AF_INET, SOCK_STREAM)
SERVER.bind(ADDRESS)

if __name__ == "__main__":
    SERVER.listen(5)
    print("Ready for connections...")
    ACCEPT_THREAD = Thread(target=get_connections)
    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join()
    SERVER.close()
