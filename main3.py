import sys
from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget
from PyQt5.QtCore import pyqtSlot, QFile, QTextStream

from Mainwindow3 import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.icon_only_widget.hide()
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.full_home_btn.setChecked(True)
        self.ui.stacked_bay.setCurrentIndex(0)
        self.ui.locasort_a_btn.setChecked(True)

        
    
    # def on_search_btn_clicked(self):
    #     self.ui.stackedWidget.setCurrentIndex(5)
    #     search_text = self.ui.search_input.text().strip()
    #     if search_text:

    def on_listsort_btn_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(0)
        
    def on_locationsort_btn_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(6)
    
    def on_icon_home_btn_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(0)

    def on_full_home_btn_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(0)

    def on_icon_dashboard_btn_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(1)

    def on_full_dashboard_btn_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(1)

    def on_icon_accept_btn_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(2)

    def on_full_accept_btn_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(2)

    def on_icon_edit_btn_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(3)

    def on_full_edit_btn_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(3)

    def on_icon_monitor_btn_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(4)

    def on_full_monitor_btn_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(4)

    #locationsort_page_btn
    def on_locasort_a_btn_toggled(self):
        self.ui.stacked_bay.setCurrentIndex(0)
    def on_locasort_b_btn_toggled(self):
        self.ui.stacked_bay.setCurrentIndex(1)
    def on_locasort_c_btn_toggled(self):
        self.ui.stacked_bay.setCurrentIndex(2)
    def on_locasort_d_btn_toggled(self):
        self.ui.stacked_bay.setCurrentIndex(3)
    def on_locasort_e_btn_toggled(self):
        self.ui.stacked_bay.setCurrentIndex(4)
    def on_locasort_f_btn_toggled(self):
        self.ui.stacked_bay.setCurrentIndex(5)
    def on_locasort_g_btn_toggled(self):
        self.ui.stacked_bay.setCurrentIndex(6)
    def on_locasort_h_btn_toggled(self):
        self.ui.stacked_bay.setCurrentIndex(7)

        




if __name__ =="__main__":
    app = QApplication(sys.argv)

    style_file = QFile("style2.qss")
    style_file.open(QFile.ReadOnly | QFile.Text)
    style_stream = QTextStream(style_file)
    app.setStyleSheet(style_stream.readAll())

    window = MainWindow()
    window.show()

    sys.exit(app.exec())