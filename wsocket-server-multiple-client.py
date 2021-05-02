import socket
from _thread import *

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM);

# Bind and listen
serverSocket.bind(("127.0.0.1", 9090));
serverSocket.listen();
print("server runing")

def Client(clientConnected, clientAddress):
    while True:
        dataFromClient = clientConnected.recv(1024)
        print(dataFromClient.decode());
        clientConnected.send("Success!".encode());
    clientConnected.close()

while(True):
	(clientConnected, clientAddress) = serverSocket.accept();
	print("Accepted a connection request from %s:%s"%(clientAddress[0], clientAddress[1]));
	start_new_thread(Client,(clientConnected, clientAddress))

