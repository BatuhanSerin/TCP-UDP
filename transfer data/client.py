import socket                  

s = socket.socket()             
host = socket.gethostname()     
port = 60000                    

s.connect((host, port))
password=input("Please enter a password\n")
s.send(password.encode())
s.send(b'Connection succed!')

with open('received_file', 'wb') as f:
    print ('file opened')
    while True:
        print('receiving data...')
        data = s.recv(1024)
        #print('data=%s', (data))
        if not data:
            break
        f.write(data)

f.close()
print('Successfully get the file')
s.close()
print('connection closed')





