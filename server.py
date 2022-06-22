import socket 
from threading import Thread

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ipaddress = "127.0.0.1"
port = 8000
server.bind ((ipaddress, port))
server.listen ()
listOfClients = []
nicknames=[]

print("server is running")
def clientThread(conn, nickname):
    conn.send("welcome to this chat room.".encode("utf-8"))
    while True:
        try :
            message = conn.recv(2048).decode("utf-8")
            if message:
                print( message)
                broadcast(message, conn)
            else:
                remove(conn)
                remove_nickname(nickname)
        except: 
            continue

def broadcast(messsage, connection):
    for clients in listOfClients:
        if clients != connection :
            try:
                clients.send(message.encode("utf-8"))
            except: 
                remove(clients)
def remove(connection):
    if connection in listOfClients:
        listOfClients.remove(connection)

def remove_nickname(nickname):
    if nickname in nicknames:
        nicknames.remove(nickname)
        
while True: 
    conn, addr = server.accept()
    conn.send("NICKNAME". encode("utf-8"))
    nickname = conn.recv(2048).decode("utf-8")
    listOfClients.append(conn)
    nicknames.append(nickname)
    message="{} joined".format(nickname)
    print(message)
    broadcast(message, conn)
    newThread = Thread(target = clientThread, args=(conn, nickname))
    newThread.start()