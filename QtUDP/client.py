from PyQt5 import QtCore, QtGui, QtWidgets
import socket
class Client():
    
    def __init__(self,textEdit):
        
        self.textEdit=textEdit
        self.actClient()
        
    def actClient(self):
        s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)     

        host = socket.gethostname()		
        port = 60000			       
        msg = self.textEdit.toPlainText()
        #msg = b'Hello Python!'
        print ("UDP target IP:", host)
        print ("UDP target Port:", port)
        
        s.sendto(msg.encode(),(host,port))		
        


        