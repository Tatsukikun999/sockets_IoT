import socket
import threading
import sys 

PORT = 7500
BUFSIZE = 4096
SERVERIP = 'localhost' #server IP

def server_handler(client):
	while True:
		try:
			data = client.recv(BUFSIZE) # data from server
		except:
			print('xaou')
			break
		if (not data) or (data.decode('utf-8') == 'q' ):
			print('xaou enough!')
			break

		print('USER: ',data.decode('utf-8'))

	client.close()

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)

try:
	client.connect((SERVERIP,PORT))
except:
	print('ERROR! xaou')
	sys.exit()

task = threading.Thread(target=server_handler,args=(client,))
task.start()

while True:
	msg = input('Message: ')
	client.sendall(msg.encode('utf_8'))
	if msg == 'q':
		break
client.close()
