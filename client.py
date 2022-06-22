import socket 
from threading import Thread

nickname = input("Choose your nickname: ")
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ipaddress = "127.0.0.1"
port = 8000
client.connect((ipaddress,port))
print("connected with the server")
def receive():
    while True:
        try:
            message = client.recv(2048).decode("utf-8")
            if message =="NICKNAME":
                client.send(nickname.encode("utf-8"))
            else: 
                print(message)
        except:
            print("An error occured")
            client.close()
            break

def write():
    while True:
        message="{}: {}".format(nickname,input(""))
        client.send(message.encode("utf-8"))

recieveThread = Thread( target = receive )
recieveThread.start()
writeThread = Thread( target = write)
writeThread.start()