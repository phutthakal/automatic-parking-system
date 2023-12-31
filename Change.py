# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\change_bay.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Change_Bay(object):
    def setupUi(self, Change_Bay):
        Change_Bay.setObjectName("Change_Bay")
        Change_Bay.resize(1200, 700)
        Change_Bay.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(Change_Bay)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(7)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setSpacing(10)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.input_frame = QtWidgets.QFrame(self.frame)
        self.input_frame.setMaximumSize(QtCore.QSize(250, 16777215))
        self.input_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.input_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.input_frame.setObjectName("input_frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.input_frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_4 = QtWidgets.QFrame(self.input_frame)
        self.frame_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setFamily("Mitr SemiBold")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.frame_4)
        font = QtGui.QFont()
        font.setFamily("Mitr SemiBold")
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("border: none;\n"
"padding: 10px;\n"
"color: #F7F7F7;\n"
"background-color: #580EF6;\n"
"border-radius: 20px;")
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_2.addWidget(self.lineEdit)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_40 = QtWidgets.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setFamily("Mitr SemiBold")
        font.setPointSize(12)
        self.label_40.setFont(font)
        self.label_40.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_40.setObjectName("label_40")
        self.horizontalLayout_10.addWidget(self.label_40)
        self.wrong_zone_line_edit = QtWidgets.QLineEdit(self.frame_4)
        font = QtGui.QFont()
        font.setFamily("Mitr SemiBold")
        font.setPointSize(10)
        self.wrong_zone_line_edit.setFont(font)
        self.wrong_zone_line_edit.setStyleSheet("border: none;\n"
"padding: 10px;\n"
"color: #F7F7F7;\n"
"background-color: #580EF6;\n"
"border-radius: 20px;")
        self.wrong_zone_line_edit.setObjectName("wrong_zone_line_edit")
        self.horizontalLayout_10.addWidget(self.wrong_zone_line_edit)
        self.verticalLayout_2.addLayout(self.horizontalLayout_10)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.status_check_label1 = QtWidgets.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setFamily("Mitr SemiBold")
        font.setPointSize(12)
        self.status_check_label1.setFont(font)
        self.status_check_label1.setStyleSheet("color: rgb(0, 170, 0);")
        self.status_check_label1.setText("")
        self.status_check_label1.setObjectName("status_check_label1")
        self.verticalLayout_2.addWidget(self.status_check_label1)
        self.load_db_btn = QtWidgets.QPushButton(self.frame_4)
        font = QtGui.QFont()
        font.setFamily("Mitr SemiBold")
        font.setPointSize(12)
        self.load_db_btn.setFont(font)
        self.load_db_btn.setStyleSheet("#load_db_btn{\n"
"    border: none;\n"
"    padding: 10px;\n"
"    background-color: #580EF6;\n"
"    color: #F0F8FF;\n"
"    border-radius: 20px;\n"
"}\n"
"#load_db_btn:hover{\n"
"    border: none;\n"
"    padding: 10px;\n"
"    background-color: #F0F8FF;\n"
"    color: #000000;\n"
"    border-radius: 20px;\n"
"}")
        self.load_db_btn.setObjectName("load_db_btn")
        self.verticalLayout_2.addWidget(self.load_db_btn)
        self.accept_new_btn = QtWidgets.QPushButton(self.frame_4)
        font = QtGui.QFont()
        font.setFamily("Mitr SemiBold")
        font.setPointSize(12)
        self.accept_new_btn.setFont(font)
        self.accept_new_btn.setStyleSheet("#accept_new_btn{\n"
"    border: none;\n"
"    padding: 10px;\n"
"    background-color: #580EF6;\n"
"    color: #F0F8FF;\n"
"    border-radius: 20px;\n"
"}\n"
"#accept_new_btn:hover{\n"
"    border: none;\n"
"    padding: 10px;\n"
"    background-color: #F0F8FF;\n"
"    color: #000000;\n"
"    border-radius: 20px;\n"
"}")
        self.accept_new_btn.setObjectName("accept_new_btn")
        self.verticalLayout_2.addWidget(self.accept_new_btn)
        self.clear_btn = QtWidgets.QPushButton(self.frame_4)
        font = QtGui.QFont()
        font.setFamily("Mitr SemiBold")
        font.setPointSize(12)
        self.clear_btn.setFont(font)
        self.clear_btn.setStyleSheet("#clear_btn{\n"
"    border: none;\n"
"    padding: 10px;\n"
"    background-color: #580EF6;\n"
"    color: #F0F8FF;\n"
"    border-radius: 20px;\n"
"}\n"
"#clear_btn:hover{\n"
"    border: none;\n"
"    padding: 10px;\n"
"    background-color: #F0F8FF;\n"
"    color: #000000;\n"
"    border-radius: 20px;\n"
"}")
        self.clear_btn.setObjectName("clear_btn")
        self.verticalLayout_2.addWidget(self.clear_btn)
        self.verticalLayout.addWidget(self.frame_4)
        self.horizontalLayout_9.addWidget(self.input_frame)
        self.now_frame = QtWidgets.QFrame(self.frame)
        self.now_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.now_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.now_frame.setObjectName("now_frame")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.now_frame)
        self.verticalLayout_4.setContentsMargins(10, 20, 10, 20)
        self.verticalLayout_4.setSpacing(8)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.content_now_frame = QtWidgets.QFrame(self.now_frame)
        self.content_now_frame.setStyleSheet("background-color: #580EF6;\n"
"border-radius: 20px;")
        self.content_now_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.content_now_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.content_now_frame.setObjectName("content_now_frame")
        self.verticalLayout_19 = QtWidgets.QVBoxLayout(self.content_now_frame)
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.frame_5 = QtWidgets.QFrame(self.content_now_frame)
        self.frame_5.setMaximumSize(QtCore.QSize(16777215, 60))
        self.frame_5.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.header_now_label = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setFamily("Mitr SemiBold")
        font.setPointSize(17)
        self.header_now_label.setFont(font)
        self.header_now_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.header_now_label.setAlignment(QtCore.Qt.AlignCenter)
        self.header_now_label.setObjectName("header_now_label")
        self.horizontalLayout_3.addWidget(self.header_now_label)
        self.verticalLayout_19.addWidget(self.frame_5)
        self.frame_7 = QtWidgets.QFrame(self.content_now_frame)
        self.frame_7.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_7)
        self.verticalLayout_3.setSpacing(20)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_9 = QtWidgets.QFrame(self.frame_7)
        self.frame_9.setStyleSheet("background-color: #F0F8FF;\n"
"border-radius: 20px;")
        self.frame_9.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_9)
        self.horizontalLayout_5.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.frame_11 = QtWidgets.QFrame(self.frame_9)
        self.frame_11.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_11)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_4 = QtWidgets.QLabel(self.frame_11)
        font = QtGui.QFont()
        font.setFamily("Mitr SemiBold")
        font.setPointSize(16)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_5.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.frame_11)
        font = QtGui.QFont()
        font.setFamily("Mitr SemiBold")
        font.setPointSize(16)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_5.addWidget(self.label_5)
        self.old_license_plate_label = QtWidgets.QLabel(self.frame_11)
        font = QtGui.QFont()
        font.setFamily("Mitr SemiBold")
        font.setPointSize(16)
        self.old_license_plate_label.setFont(font)
        self.old_license_plate_label.setAlignment(QtCore.Qt.AlignCenter)
        self.old_license_plate_label.setObjectName("old_license_plate_label")
        self.verticalLayout_5.addWidget(self.old_license_plate_label)
        self.horizontalLayout_5.addWidget(self.frame_11)
        self.frame_12 = QtWidgets.QFrame(self.frame_9)
        self.frame_12.setMaximumSize(QtCore.QSize(30, 16777215))
        self.frame_12.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_12)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_9 = QtWidgets.QLabel(self.frame_12)
        font = QtGui.QFont()
        font.setFamily("Mitr SemiBold")
        font.setPointSize(16)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_6.addWidget(self.label_9)
        self.label_10 = QtWidgets.QLabel(self.frame_12)
        font = QtGui.QFont()
        font.setFamily("Mitr SemiBold")
        font.setPointSize(16)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_6.addWidget(self.label_10)
        self.label_8 = QtWidgets.QLabel(self.frame_12)
        font = QtGui.QFont()
        font.setFamily("Mitr SemiBold")
        font.setPointSize(16)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_6.addWidget(self.label_8)
        self.horizontalLayout_5.addWidget(self.frame_12)
        self.frame_13 = QtWidgets.QFrame(self.frame_9)
        self.frame_13.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_13)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_11 = QtWidgets.QLabel(self.frame_13)
        font = QtGui.QFont()
        font.setFamily("Mitr SemiBold")
        font.setPointSize(16)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_11.setText("")
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_7.addWidget(self.label_11)
        self.label_12 = QtWidgets.QLabel(self.frame_13)
        font = QtGui.QFont()
        font.setFamily("Mitr SemiBold")
        font.setPointSize(16)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_12.setText("")
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_7.addWidget(self.label_12)
        self.label_13 = QtWidgets.QLabel(self.frame_13)
        font = QtGui.QFont()
        font.setFamily("Mitr SemiBold")
        font.setPointSize(16)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_13.setText("")
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_7.addWidget(self.label_13)
        self.horizontalLayout_5.addWidget(self.frame_13)
        self.verticalLayout_3.addWidget(self.frame_9)
        self.frame_10 = QtWidgets.QFrame(self.frame_7)
        self.frame_10.setStyleSheet("background-color: #F0F8FF;\n"
"border-radius: 20px;")
        self.frame_10.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_10)
        self.horizontalLayout_7.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.frame_14 = QtWidgets.QFrame(self.frame_10)
        self.frame_14.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_14.setObjectName("frame_14")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.frame_14)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.label_26 = QtWidgets.QLabel(self.frame_14)
        font = QtGui.QFont()
        font.setFamily("Mitr SemiBold")
        font.setPointSize(16)
        self.label_26.setFont(font)
        self.label_26.setAlignment(QtCore.Qt.AlignCenter)
        self.label_26.setObjectName("label_26")
        self.verticalLayout_13.addWidget(self.label_26)
        self.label_7 = QtWidgets.QLabel(self.frame_14)
        font = QtGui.QFont()
        font.setFamily("Mitr SemiBold")
        font.setPointSize(16)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_13.addWidget(self.label_7)
        self.label_27 = QtWidgets.QLabel(self.frame_14)
        font = QtGui.QFont()
        font.setFamily("Mitr SemiBold")
        font.setPointSize(16)
        self.label_27.setFont(font)
        self.label_27.setAlignment(QtCore.Qt.AlignCenter)
        self.label_27.setObjectName("label_27")
        self.verticalLayout_13.addWidget(self.label_27)
        self.horizontalLayout_7.addWidget(self.frame_14)
        self.frame_20 = QtWidgets.QFrame(self.frame_10)
        self.frame_20.setMaximumSize(QtCore.QSize(30, 16777215))
        self.frame_20.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_20.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_20.setObjectName("frame_20")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.frame_20)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.label_23 = QtWidgets.QLabel(self.frame_20)
        font = QtGui.QFont()
        font.setFamily("Mitr SemiBold")
        font.setPointSize(16)
        self.label_23.setFont(font)
        self.label_23.setAlignment(QtCore.Qt.AlignCenter)
        self.label_23.setObjectName("label_23")
        self.verticalLayout_12.addWidget(self.label_23)
        self.label_24 = QtWidgets.QLabel(self.frame_20)
        font = QtGui.QFont()
        font.setFamily("Mitr SemiBold")
        font.setPointSize(16)
        self.label_24.setFont(font)
        self.label_24.setAlignment(QtCore.Qt.AlignCenter)
        self.label_24.setObjectName("label_24")
        self.verticalLayout_12.addWidget(self.label_24)
        self.label_25 = QtWidgets.QLabel(self.frame_20)
        font = QtGui.QFont()
        font.setFamily("Mitr SemiBold")
        font.setPointSize(16)
        self.label_25.setFont(font)
        self.label_25.setAlignment(QtCore.Qt.AlignCenter)
        self.label_25.setObjectName("label_25")
        self.verticalLayout_12.addWidget(self.label_25)
        self.horizontalLayout_7.addWidget(self.frame_20)
        self.frame_21 = QtWidgets.QFrame(self.frame_10)
        self.frame_21.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_21.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_21.setObjectName("frame_21")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.frame_21)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.label_28 = QtWidgets.QLabel(self.frame_21)
        font = QtGui.QFont()
        font.setFamily("Mitr SemiBold")
        font.setPointSize(16)
        self.label_28.setFont(font)
        self.label_28.setStyleSheet("color: #FF0000;")
        self.label_28.setText("")
        self.label_28.setAlignment(QtCore.Qt.AlignCenter)
        self.label_28.setObjectName("label_28")
        self.verticalLayout_14.addWidget(self.label_28)
        self.label_29 = QtWidgets.QLabel(self.frame_21)
        font = QtGui.QFont()
        font.setFamily("Mitr SemiBold")
        font.setPointSize(16)
        self.label_29.setFont(font)
        self.label_29.setStyleSheet("color: #FF0000;")
        self.label_29.setText("")
        self.label_29.setAlignment(QtCore.Qt.AlignCenter)
        self.label_29.setObjectName("label_29")
        self.verticalLayout_14.addWidget(self.label_29)
        self.label_30 = QtWidgets.QLabel(self.frame_21)
        font = QtGui.QFont()
        font.setFamily("Mitr SemiBold")
        font.setPointSize(16)
        self.label_30.setFont(font)
        self.label_30.setStyleSheet("color: #FF0000;")
        self.label_30.setText("")
        self.label_30.setAlignment(QtCore.Qt.AlignCenter)
        self.label_30.setObjectName("label_30")
        self.verticalLayout_14.addWidget(self.label_30)
        self.horizontalLayout_7.addWidget(self.frame_21)
        self.verticalLayout_3.addWidget(self.frame_10)
        self.verticalLayout_19.addWidget(self.frame_7)
        self.verticalLayout_4.addWidget(self.content_now_frame)
        self.horizontalLayout_9.addWidget(self.now_frame)
        self.new_frame = QtWidgets.QFrame(self.frame)
        self.new_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.new_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.new_frame.setObjectName("new_frame")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.new_frame)
        self.verticalLayout_8.setContentsMargins(10, 20, 20, 20)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.content_new_frame = QtWidgets.QFrame(self.new_frame)
        self.content_new_frame.setStyleSheet("background-color: #580EF6;\n"
"border-radius: 20px;")
        self.content_new_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.content_new_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.content_new_frame.setObjectName("content_new_frame")
        self.verticalLayout_20 = QtWidgets.QVBoxLayout(self.content_new_frame)
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.head_new_frame_6 = QtWidgets.QFrame(self.content_new_frame)
        self.head_new_frame_6.setMaximumSize(QtCore.QSize(16777215, 60))
        self.head_new_frame_6.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.head_new_frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.head_new_frame_6.setObjectName("head_new_frame_6")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.head_new_frame_6)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.header_new_lot_label = QtWidgets.QLabel(self.head_new_frame_6)
        font = QtGui.QFont()
        font.setFamily("Mitr SemiBold")
        font.setPointSize(17)
        self.header_new_lot_label.setFont(font)
        self.header_new_lot_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.header_new_lot_label.setAlignment(QtCore.Qt.AlignCenter)
        self.header_new_lot_label.setObjectName("header_new_lot_label")
        self.horizontalLayout_4.addWidget(self.header_new_lot_label)
        self.verticalLayout_20.addWidget(self.head_new_frame_6)
        self.frame_8 = QtWidgets.QFrame(self.content_new_frame)
        self.frame_8.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.verticalLayout_18 = QtWidgets.QVBoxLayout(self.frame_8)
        self.verticalLayout_18.setSpacing(20)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.frame_15 = QtWidgets.QFrame(self.frame_8)
        self.frame_15.setStyleSheet("background-color: #F0F8FF;\n"
"border-radius: 20px;")
        self.frame_15.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_15.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_15.setObjectName("frame_15")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_15)
        self.horizontalLayout_6.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.frame_19 = QtWidgets.QFrame(self.frame_15)
        self.frame_19.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_19.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_19.setObjectName("frame_19")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.frame_19)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.label_20 = QtWidgets.QLabel(self.frame_19)
        font = QtGui.QFont()
        font.setFamily("Mitr SemiBold")
        font.setPointSize(16)
        self.label_20.setFont(font)
        self.label_20.setAlignment(QtCore.Qt.AlignCenter)
        self.label_20.setObjectName("label_20")
        self.verticalLayout_11.addWidget(self.label_20)
        self.label_21 = QtWidgets.QLabel(self.frame_19)
        font = QtGui.QFont()
        font.setFamily("Mitr SemiBold")
        font.setPointSize(16)
        self.label_21.setFont(font)
        self.label_21.setAlignment(QtCore.Qt.AlignCenter)
        self.label_21.setObjectName("label_21")
        self.verticalLayout_11.addWidget(self.label_21)
        self.label_22 = QtWidgets.QLabel(self.frame_19)
        font = QtGui.QFont()
        font.setFamily("Mitr SemiBold")
        font.setPointSize(16)
        self.label_22.setFont(font)
        self.label_22.setAlignment(QtCore.Qt.AlignCenter)
        self.label_22.setObjectName("label_22")
        self.verticalLayout_11.addWidget(self.label_22)
        self.horizontalLayout_6.addWidget(self.frame_19)
        self.frame_18 = QtWidgets.QFrame(self.frame_15)
        self.frame_18.setMaximumSize(QtCore.QSize(30, 16777215))
        self.frame_18.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_18.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_18.setObjectName("frame_18")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.frame_18)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_14 = QtWidgets.QLabel(self.frame_18)
        font = QtGui.QFont()
        font.setFamily("Mitr SemiBold")
        font.setPointSize(16)
        self.label_14.setFont(font)
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.verticalLayout_9.addWidget(self.label_14)
        self.label_15 = QtWidgets.QLabel(self.frame_18)
        font = QtGui.QFont()
        font.setFamily("Mitr SemiBold")
        font.setPointSize(16)
        self.label_15.setFont(font)
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.verticalLayout_9.addWidget(self.label_15)
        self.label_16 = QtWidgets.QLabel(self.frame_18)
        font = QtGui.QFont()
        font.setFamily("Mitr SemiBold")
        font.setPointSize(16)
        self.label_16.setFont(font)
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.verticalLayout_9.addWidget(self.label_16)
        self.horizontalLayout_6.addWidget(self.frame_18)
        self.frame_17 = QtWidgets.QFrame(self.frame_15)
        self.frame_17.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_17.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_17.setObjectName("frame_17")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.frame_17)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.new_card_id_label = QtWidgets.QLabel(self.frame_17)
        font = QtGui.QFont()
        font.setFamily("Mitr SemiBold")
        font.setPointSize(16)
        self.new_card_id_label.setFont(font)
        self.new_card_id_label.setStyleSheet("color: rgb(0, 0, 0);")
        self.new_card_id_label.setText("")
        self.new_card_id_label.setAlignment(QtCore.Qt.AlignCenter)
        self.new_card_id_label.setObjectName("new_card_id_label")
        self.verticalLayout_10.addWidget(self.new_card_id_label)
        self.new_height_label = QtWidgets.QLabel(self.frame_17)
        font = QtGui.QFont()
        font.setFamily("Mitr SemiBold")
        font.setPointSize(16)
        self.new_height_label.setFont(font)
        self.new_height_label.setStyleSheet("color: rgb(0, 0, 0);")
        self.new_height_label.setText("")
        self.new_height_label.setAlignment(QtCore.Qt.AlignCenter)
        self.new_height_label.setObjectName("new_height_label")
        self.verticalLayout_10.addWidget(self.new_height_label)
        self.new_license_p_label = QtWidgets.QLabel(self.frame_17)
        font = QtGui.QFont()
        font.setFamily("Mitr SemiBold")
        font.setPointSize(16)
        self.new_license_p_label.setFont(font)
        self.new_license_p_label.setStyleSheet("color: rgb(0, 0, 0);")
        self.new_license_p_label.setText("")
        self.new_license_p_label.setAlignment(QtCore.Qt.AlignCenter)
        self.new_license_p_label.setObjectName("new_license_p_label")
        self.verticalLayout_10.addWidget(self.new_license_p_label)
        self.horizontalLayout_6.addWidget(self.frame_17)
        self.verticalLayout_18.addWidget(self.frame_15)
        self.frame_16 = QtWidgets.QFrame(self.frame_8)
        self.frame_16.setStyleSheet("background-color: #F0F8FF;\n"
"border-radius: 20px;")
        self.frame_16.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_16.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_16.setObjectName("frame_16")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_16)
        self.horizontalLayout_8.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.frame_24 = QtWidgets.QFrame(self.frame_16)
        self.frame_24.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_24.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_24.setObjectName("frame_24")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout(self.frame_24)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.label_37 = QtWidgets.QLabel(self.frame_24)
        font = QtGui.QFont()
        font.setFamily("Mitr SemiBold")
        font.setPointSize(16)
        self.label_37.setFont(font)
        self.label_37.setAlignment(QtCore.Qt.AlignCenter)
        self.label_37.setObjectName("label_37")
        self.verticalLayout_17.addWidget(self.label_37)
        self.label_38 = QtWidgets.QLabel(self.frame_24)
        font = QtGui.QFont()
        font.setFamily("Mitr SemiBold")
        font.setPointSize(16)
        self.label_38.setFont(font)
        self.label_38.setAlignment(QtCore.Qt.AlignCenter)
        self.label_38.setObjectName("label_38")
        self.verticalLayout_17.addWidget(self.label_38)
        self.label_39 = QtWidgets.QLabel(self.frame_24)
        font = QtGui.QFont()
        font.setFamily("Mitr SemiBold")
        font.setPointSize(16)
        self.label_39.setFont(font)
        self.label_39.setAlignment(QtCore.Qt.AlignCenter)
        self.label_39.setObjectName("label_39")
        self.verticalLayout_17.addWidget(self.label_39)
        self.horizontalLayout_8.addWidget(self.frame_24)
        self.frame_23 = QtWidgets.QFrame(self.frame_16)
        self.frame_23.setMaximumSize(QtCore.QSize(30, 16777215))
        self.frame_23.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_23.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_23.setObjectName("frame_23")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.frame_23)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.label_34 = QtWidgets.QLabel(self.frame_23)
        font = QtGui.QFont()
        font.setFamily("Mitr SemiBold")
        font.setPointSize(16)
        self.label_34.setFont(font)
        self.label_34.setAlignment(QtCore.Qt.AlignCenter)
        self.label_34.setObjectName("label_34")
        self.verticalLayout_16.addWidget(self.label_34)
        self.label_35 = QtWidgets.QLabel(self.frame_23)
        font = QtGui.QFont()
        font.setFamily("Mitr SemiBold")
        font.setPointSize(16)
        self.label_35.setFont(font)
        self.label_35.setAlignment(QtCore.Qt.AlignCenter)
        self.label_35.setObjectName("label_35")
        self.verticalLayout_16.addWidget(self.label_35)
        self.label_36 = QtWidgets.QLabel(self.frame_23)
        font = QtGui.QFont()
        font.setFamily("Mitr SemiBold")
        font.setPointSize(16)
        self.label_36.setFont(font)
        self.label_36.setAlignment(QtCore.Qt.AlignCenter)
        self.label_36.setObjectName("label_36")
        self.verticalLayout_16.addWidget(self.label_36)
        self.horizontalLayout_8.addWidget(self.frame_23)
        self.frame_22 = QtWidgets.QFrame(self.frame_16)
        self.frame_22.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_22.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_22.setObjectName("frame_22")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.frame_22)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.new_zone_label = QtWidgets.QLabel(self.frame_22)
        font = QtGui.QFont()
        font.setFamily("Mitr SemiBold")
        font.setPointSize(16)
        self.new_zone_label.setFont(font)
        self.new_zone_label.setStyleSheet("color: rgb(0, 170, 0);")
        self.new_zone_label.setText("")
        self.new_zone_label.setAlignment(QtCore.Qt.AlignCenter)
        self.new_zone_label.setObjectName("new_zone_label")
        self.verticalLayout_15.addWidget(self.new_zone_label)
        self.new_bay_label = QtWidgets.QLabel(self.frame_22)
        font = QtGui.QFont()
        font.setFamily("Mitr SemiBold")
        font.setPointSize(16)
        self.new_bay_label.setFont(font)
        self.new_bay_label.setStyleSheet("color: rgb(0, 170, 0);")
        self.new_bay_label.setText("")
        self.new_bay_label.setAlignment(QtCore.Qt.AlignCenter)
        self.new_bay_label.setObjectName("new_bay_label")
        self.verticalLayout_15.addWidget(self.new_bay_label)
        self.new_lot_label = QtWidgets.QLabel(self.frame_22)
        font = QtGui.QFont()
        font.setFamily("Mitr SemiBold")
        font.setPointSize(16)
        self.new_lot_label.setFont(font)
        self.new_lot_label.setStyleSheet("color: rgb(0, 170, 0);")
        self.new_lot_label.setText("")
        self.new_lot_label.setAlignment(QtCore.Qt.AlignCenter)
        self.new_lot_label.setObjectName("new_lot_label")
        self.verticalLayout_15.addWidget(self.new_lot_label)
        self.horizontalLayout_8.addWidget(self.frame_22)
        self.verticalLayout_18.addWidget(self.frame_16)
        self.verticalLayout_20.addWidget(self.frame_8)
        self.verticalLayout_8.addWidget(self.content_new_frame)
        self.horizontalLayout_9.addWidget(self.new_frame)
        self.horizontalLayout.addWidget(self.frame)
        Change_Bay.setCentralWidget(self.centralwidget)

        self.retranslateUi(Change_Bay)
        QtCore.QMetaObject.connectSlotsByName(Change_Bay)

    def retranslateUi(self, Change_Bay):
        _translate = QtCore.QCoreApplication.translate
        Change_Bay.setWindowTitle(_translate("Change_Bay", "Change_Bay"))
        self.label.setText(_translate("Change_Bay", "การ์ดไอดี :"))
        self.label_40.setText(_translate("Change_Bay", "โซนที่เข้าผิด :"))
        self.load_db_btn.setText(_translate("Change_Bay", "โหลดข้อมูลจากการ์ด"))
        self.accept_new_btn.setText(_translate("Change_Bay", "รับช่องจอดใหม่"))
        self.clear_btn.setText(_translate("Change_Bay", "เคลียร์ข้อมูล"))
        self.header_now_label.setText(_translate("Change_Bay", "ช่องจอดปัจจุบัน"))
        self.label_4.setText(_translate("Change_Bay", "การ์ดไอดี"))
        self.label_5.setText(_translate("Change_Bay", "ความสูง"))
        self.old_license_plate_label.setText(_translate("Change_Bay", "ทะเบียน"))
        self.label_9.setText(_translate("Change_Bay", ":"))
        self.label_10.setText(_translate("Change_Bay", ":"))
        self.label_8.setText(_translate("Change_Bay", ":"))
        self.label_26.setText(_translate("Change_Bay", "โซน"))
        self.label_7.setText(_translate("Change_Bay", "ช่องจอด"))
        self.label_27.setText(_translate("Change_Bay", "หมายเลข"))
        self.label_23.setText(_translate("Change_Bay", ":"))
        self.label_24.setText(_translate("Change_Bay", ":"))
        self.label_25.setText(_translate("Change_Bay", ":"))
        self.header_new_lot_label.setText(_translate("Change_Bay", "ช่องจอดใหม่"))
        self.label_20.setText(_translate("Change_Bay", "การ์ดไอดี"))
        self.label_21.setText(_translate("Change_Bay", "ความสูง"))
        self.label_22.setText(_translate("Change_Bay", "ทะเบียน"))
        self.label_14.setText(_translate("Change_Bay", ":"))
        self.label_15.setText(_translate("Change_Bay", ":"))
        self.label_16.setText(_translate("Change_Bay", ":"))
        self.label_37.setText(_translate("Change_Bay", "โซน"))
        self.label_38.setText(_translate("Change_Bay", "ช่องจอด"))
        self.label_39.setText(_translate("Change_Bay", "หมายเลข"))
        self.label_34.setText(_translate("Change_Bay", ":"))
        self.label_35.setText(_translate("Change_Bay", ":"))
        self.label_36.setText(_translate("Change_Bay", ":"))
