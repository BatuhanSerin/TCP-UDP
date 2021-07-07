import socket

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)      

host = socket.gethostname()		        
port = 60000			                

s.bind((host,port))

while True:
	print ("Waiting for client...")
	data,addr = s.recvfrom(1024)	        #receive data from client
	print ("Received Messages:",data," from",addr)





