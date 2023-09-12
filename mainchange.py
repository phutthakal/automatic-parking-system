import sys
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget
from PyQt5.QtCore import pyqtSlot, QFile, QTextStream 
import mysql.connector as mc
from PyQt5.QtCore import QTimer


from Change import *

class MainBigWindow(QMainWindow):
    def __init__(self):
        super(MainBigWindow, self).__init__()

        self.ui = Ui_Change_Bay()
        self.ui.setupUi(self)
        # self.showFullScreen()
        
        #flamelesswindow
        # self.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    style_file = QFile("stylechange.qss")
    style_file.open(QFile.ReadOnly | QFile.Text)
    style_stream = QTextStream(style_file)
    app.setStyleSheet(style_stream.readAll())
    
    bigwindow = MainBigWindow()
    bigwindow.show()
     
    sys.exit(app.exec())

    