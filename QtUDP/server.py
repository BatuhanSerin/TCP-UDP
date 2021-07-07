import socket
class Server():
    
    def __init__(self,label,flag):
        
        self.label=label
        self.flag=flag
        self.act()
        
    def act(self):
        self.s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)      

        self.host = socket.gethostname()		        
        self.port = 60000			                
        
        self.s.bind((self.host,self.port))
        
            
        print ("Waiting for client...")
        if self.flag == 1:
            
            self.label.setText("Waiting for client...")
            self.data , self.addr = self.s.recvfrom(1024)	        
            print ("Received Messages:",self.data," from",self.addr)
            self.label.setText(repr(self.data))
       

        
