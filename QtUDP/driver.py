from PyQt5 import QtWidgets
 
from UDP import Ui_Form  
 
import sys
 
class mywindow(QtWidgets.QWidget):
 
    def __init__(self):
 
        super(mywindow, self).__init__()
 
        self.ui = Ui_Form()
    
        self.ui.setupUi(self)
 
app = QtWidgets.QApplication([])
 
application = mywindow()
 
application.show()
 
sys.exit(app.exec())