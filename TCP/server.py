import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((socket.gethostname(),1024))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print("connected by", addr)
        while True:
            data1 = conn.recv(1024)
            if data1 !=b'pass':
                print(addr,"has been kicked!")
                break
            data = conn.recv(1024)
            if not data :
                break
            conn.sendall(data)








