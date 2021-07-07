import socket                   

port = 60000                   
s = socket.socket()             
host = socket.gethostname()     
s.bind((host, port))            
s.listen()                     

print ('Server listening....')

while True:
    conn, addr = s.accept()     
    data1 = conn.recv(1024)
    if data1 !=b'pass':
        print(addr,"has been kicked!")
        break
    
    print ('Got connection from', addr)
    data = conn.recv(1024)
    print('Server received', str(data,"utf-8"))

    filename='mytext.txt'
    f = open(filename,'rb')
    l = f.read(1024)
    while (l):
       conn.send(l)
       print('Sent \n',str(l,"utf-8"))
       l = f.read(1024)
    f.close()

    print('Sending completed')
    conn.close()
    break


