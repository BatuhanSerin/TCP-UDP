# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UDP.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import server
import client
import socket

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(552, 423)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.comboBox = QtWidgets.QComboBox(Form)
        
        font = QtGui.QFont()
        font.setPointSize(13)
        
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        
        self.gridLayout.addWidget(self.comboBox, 0, 0, 1, 1)
        
        self.stackedWidget = QtWidgets.QStackedWidget(Form)
        self.stackedWidget.setEnabled(True)
        self.stackedWidget.setObjectName("stackedWidget")
        
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        
        self.label = QtWidgets.QLabel(self.page)
        self.label.setGeometry(QtCore.QRect(10, 20, 501, 341))
        
        font = QtGui.QFont()
        font.setPointSize(13)
        
        self.label.setFont(font)
        self.label.setText("")
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label.setObjectName("label")
        
        self.stackedWidget.addWidget(self.page)
        
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        
        self.widget = QtWidgets.QWidget(self.page_2)
        self.widget.setGeometry(QtCore.QRect(0, 10, 531, 351))
        self.widget.setObjectName("widget")
        
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        
        self.pushButton = QtWidgets.QPushButton(self.widget)
        
        font = QtGui.QFont()
        font.setPointSize(13)
        
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("PushButton")
        
        self.gridLayout_2.addWidget(self.pushButton, 2, 0, 1, 1)
        
        self.textEdit = QtWidgets.QTextEdit(self.widget)
        
        font = QtGui.QFont()
        font.setPointSize(12)
        
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        
        self.gridLayout_2.addWidget(self.textEdit, 1, 0, 1, 1)
        
        self.stackedWidget.addWidget(self.page_2)
        
        self.gridLayout.addWidget(self.stackedWidget, 1, 0, 1, 1)

        self.retranslateUi(Form)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Form)
        
        self.comboBox.activated[str].connect(self.activated)
        
        self.stackedWidget.setCurrentIndex(0)
        self.flag = 0
        self.serv = server.Server(self.label,self.flag)
        
    def activated(self):
        
        if self.comboBox.currentIndex() == 0 :
            
            self.stackedWidget.setCurrentIndex(0)
            
            if self.flag == 1:
            
                self.label.setText("Waiting for client...")
                self.data , self.addr = self.serv.s.recvfrom(1024)	        
                print ("Received Messages:",str(self.data,"utf-8")," from",self.addr)
                self.label.setText(str(self.data,"utf-8"))
            
            
        else :
            self.stackedWidget.setCurrentIndex(1)
            self.pushButton.clicked.connect(self.clientAct)
            
        
    def clientAct(self):
        self.c = client.Client(self.textEdit)
        self.flag = 1

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "UDP"))
        self.comboBox.setItemText(0, _translate("Form", "Server"))
        self.comboBox.setItemText(1, _translate("Form", "CLient"))
        self.pushButton.setText(_translate("Form", "Send Message"))


class mywindow(QtWidgets.QWidget):
    
    def __init__(self):
        super(mywindow,self).__init__()
        self.ui=Ui_Form()
        self.ui.setupUi(self)
        
app = QtWidgets.QApplication([])

application = mywindow()

application.show()

sys.exit(app.exec())
