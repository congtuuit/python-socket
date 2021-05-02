import socket

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
clientSocket.connect(("127.0.0.1", 9090));

def send(clientSocket, data):
	clientSocket.send(data.encode());
	dataFromServer = clientSocket.recv(1024);
	print(dataFromServer.decode())

while True:
	data = input('Enter: ')
	if (data == "Bye" or data == "bye"):
		break

	send(clientSocket, data)

clientSocket.close()
