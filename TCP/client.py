import socket

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    s.connect((socket.gethostname(),1024))
    password=input("Please enter a password\n")
    s.send(password.encode())
    
    message="Hello"
    s.sendall(message.encode())
    
    data=s.recv(1024)
    
print("recieved\n", repr(data))
    




