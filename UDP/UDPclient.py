import socket

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)      

host = socket.gethostname()		
port = 60000			        

msg = b'Hello Python!'
print ("UDP target IP:", host)
print ("UDP target Port:", port)

s.sendto(msg,(host,port))		








