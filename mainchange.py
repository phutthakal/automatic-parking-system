import sys
import time
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget
from PyQt5.QtCore import pyqtSlot, QFile, QTextStream 
import mysql.connector as mc
from PyQt5.QtCore import QTimer
import mysql.connector
import random

from Change import *


bay_order=[]
parked_lot=[]
zone_order=['1','2']
user_data=[]

a=[]
b=[]
c=[]
d=[]
e=[]
f=[]
g=[]
h=[]

oha=[]
ohb=[]
ohc=[]
ohd=[]
ohe=[]
ohf=[]
ohg=[]
ohh=[]


# nz = normal zone
nz={"A":a,"F":f,"C":c,"B":b,"G":g,"D":d,"H":h,"E":e}
nz1={"A":a,"B":b}
nz2={"C":c,"D":d,"E":e,"F":f,"G":g,"H":h}
# oz = over heigh zone
oz={"A":oha,"F":ohf,"C":ohc,"B":ohb,"G":ohg,"D":ohd,"H":ohh,"E":ohe}
oz1={"A":oha,"B":ohb}
oz2={"C":ohc,"D":ohd,"E":ohe,"F":ohf,"G":ohg,"H":ohh}
#bay
bay_zone1={"A":a,"B":b}
bay_zone2={"C":c,"D":d,"E":e,"F":f,"G":g,"H":h}
#lot
olot={"A":a,"B":b}
nlot={"C":c,"D":d,"E":e,"F":f,"G":g,"H":h}

z={"A":zone_order[0],"B":zone_order[0],"C":zone_order[1],"D":zone_order[1],"E":zone_order[1],"F":zone_order[1],"G":zone_order[1],"H":zone_order[1]}
z1={"A":zone_order[0],"B":zone_order[0]}
z2={"C":zone_order[1],"D":zone_order[1],"E":zone_order[1],"F":zone_order[1],"G":zone_order[1],"H":zone_order[1]}

mydb = mc.connect(
        host="localhost",
        user="root",
        password="",
        database="carlot"
    )

mycursor = mydb.cursor()
mycursor.execute("SELECT bay_name FROM bay")
result = mycursor.fetchall()
for row in result:
    bay_order.append(row[0])

mycursor.execute('''
                    SELECT number FROM lot 
                    WHERE status_id='1' AND bay_id='1' AND parking_type_id='1' ''')
result = mycursor.fetchall()
for lot_a in result:
    oha.append(lot_a[0])
# print(oha)

mycursor.execute('''
                    SELECT number FROM lot 
                    WHERE status_id='1' AND bay_id='1' AND parking_type_id='0' ''')
result = mycursor.fetchall()
for lot_a in result:
    a.append(lot_a[0])
# print(a)
    
mycursor.execute('''
                    SELECT number FROM lot 
                    WHERE status_id='1' AND bay_id='2' AND parking_type_id='1' ''')
result = mycursor.fetchall()
for lot_b in result:
    ohb.append(lot_b[0])
# print(ohb)

mycursor.execute('''
                    SELECT number FROM lot 
                    WHERE status_id='1' AND bay_id='2' AND parking_type_id='0' ''')
result = mycursor.fetchall()
for lot_b in result:
    b.append(lot_b[0])
# print(b)

mycursor.execute('''
                    SELECT number FROM lot 
                    WHERE status_id='1' AND bay_id='3' AND parking_type_id='1' ''')
result = mycursor.fetchall()
for lot_c in result:
    ohc.append(lot_c[0])
# print(ohc)

mycursor.execute('''
                    SELECT number FROM lot 
                    WHERE status_id='1' AND bay_id='3' AND parking_type_id='0' ''')
result = mycursor.fetchall()
for lot_c in result:
    c.append(lot_c[0])
# print(c)
    
mycursor.execute('''
                    SELECT number FROM lot 
                    WHERE status_id='1' AND bay_id='4' AND parking_type_id='1' ''')
result = mycursor.fetchall()
for lot_d in result:
    ohd.append(lot_d[0])
# print(ohd)

mycursor.execute('''
                    SELECT number FROM lot 
                    WHERE status_id='1' AND bay_id='4' AND parking_type_id='0' ''')
result = mycursor.fetchall()
for lot_d in result:
    d.append(lot_d[0])
# print(d)

mycursor.execute('''
                    SELECT number FROM lot 
                    WHERE status_id='1' AND bay_id='5' AND parking_type_id='1' ''')
result = mycursor.fetchall()
for lot_e in result:
    ohe.append(lot_e[0])
# print(ohe)

mycursor.execute('''
                    SELECT number FROM lot 
                    WHERE status_id='1' AND bay_id='5' AND parking_type_id='0' ''')
result = mycursor.fetchall()
for lot_e in result:
    e.append(lot_e[0])
# print(e)
    
mycursor.execute('''
                    SELECT number FROM lot 
                    WHERE status_id='1' AND bay_id='6' AND parking_type_id='1' ''')
result = mycursor.fetchall()
for lot_f in result:
    ohf.append(lot_f[0])
# print(ohf)

mycursor.execute('''
                    SELECT number FROM lot 
                    WHERE status_id='1' AND bay_id='6' AND parking_type_id='0' ''')
result = mycursor.fetchall()
for lot_f in result:
    f.append(lot_f[0])
# print(f)

mycursor.execute('''
                    SELECT number FROM lot 
                    WHERE status_id='1' AND bay_id='7' AND parking_type_id='1' ''')
result = mycursor.fetchall()
for lot_g in result:
    ohg.append(lot_g[0])
# print(ohg)

mycursor.execute('''
                    SELECT number FROM lot 
                    WHERE status_id='1' AND bay_id='7' AND parking_type_id='0' ''')
result = mycursor.fetchall()
for lot_g in result:
    g.append(lot_g[0])
# print(g)
    
mycursor.execute('''
                    SELECT number FROM lot 
                    WHERE status_id='1' AND bay_id='8' AND parking_type_id='1' ''')
result = mycursor.fetchall()
for lot_h in result:
    ohh.append(lot_h[0])
# print(ohh)

mycursor.execute('''
                    SELECT number FROM lot 
                    WHERE status_id='1' AND bay_id='8' AND parking_type_id='0' ''')
result = mycursor.fetchall()
for lot_h in result:
    h.append(lot_h[0])
# print(h)

class MainBigWindow(QMainWindow):
    def __init__(self):
        super(MainBigWindow, self).__init__()

        self.ui = Ui_Change_Bay()
        self.ui.setupUi(self)
        # self.showFullScreen()
        
        #flamelesswindow
        # self.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
        self.ui.load_db_btn.clicked.connect(self.fetch_data)
        self.ui.accept_new_btn.clicked.connect(self.change_lot)
        self.ui.clear_btn.clicked.connect(self.clear_data)

    
    def fetch_data(self):
        card_id = self.ui.lineEdit.text()
        try:
            mydb = mc.connect(
                host="localhost",
                user="root",
                password="",
                database="carlot"
            )
            mycursor2 = mydb.cursor()
            mycursor2.execute('''
            SELECT card.card_id, card.user_height, card.user_license_plate, lot.parked_zone, bay.bay_name, lot.number, lot.lot_id
            FROM lot
            INNER JOIN card ON lot.lot_id = card.lot_id                  
            INNER JOIN bay ON lot.bay_id = bay.bay_id
            WHERE card_id=%s
            ''', (card_id,))
            data = mycursor2.fetchone()
            print(data)
            
            if data:
                self.ui.label_11.setText(str(data[0]))
                self.ui.label_12.setText(str(data[1]))
                self.ui.label_13.setText(str(data[2]))
                
                self.ui.label_28.setText(str(data[3]))
                self.ui.label_29.setText(str(data[4]))
                self.ui.label_30.setText(str(data[5]))
                self.ui.status_check_label1.setText("ดึงข้อมูลสำเร็จ")
            else:
                self.ui.status_check_label1.setText("ไม่มีข้อมูล")
            
            for all_data in data:
                user_data.append(all_data)  

        except:
            self.ui.status_check_label1.setText("กรุณากรอกการ์ดไอดี")
        

    def change_lot(self):
        # wrong_zone = self.ui.comboBox.setCurrentText()
        wrong_zone = self.ui.wrong_zone_line_edit.text()
        try:
            if wrong_zone=="1":
                if user_data[1] <= "190" and user_data[4] in z2:
                    random_bay = random.choice([bay for bay in bay_order if bay not in z2])
                    new_zone = z1[random_bay]
                    
                    random_lot = random.choice(nz[random_bay])
                    nz[random_bay].remove(random_lot)
                elif user_data[1] > "190" and user_data[4] in z2:
                    random_bay = random.choice([bay for bay in bay_order if bay not in z2])
                    new_zone = z1[random_bay]

                    random_lot = random.choice(oz[random_bay])
                    oz[random_bay].remove(random_lot)

                #replace_new zone,bay,lot in list user_data=[]
                user_data[3] = int(new_zone)
                user_data[4] = random_bay
                user_data[5] = random_lot

                old_lot_id = user_data[5]
                # print("ก่อนดึง db ใหม่ :",old_lot_id)

                mydb = mc.connect(
                host="localhost",
                user="root",
                password="",
                database="carlot")

                mycursor2 = mydb.cursor()
                mycursor2.execute('''
                                    SELECT lot_id FROM lot WHERE number=%s
                                    ''',(old_lot_id,))
                data_id = mycursor2.fetchone()

                user_data[6] = data_id[0]
                
                
                # print("หลังดึง",data_id)
                # print("ดึงมาใหม่รอบ 2 หลังจากดึง :",user_data)

                if user_data:
                    self.ui.new_card_id_label.setText(str(user_data[0]))
                    self.ui.new_height_label.setText(str(user_data[1]))
                    self.ui.new_license_p_label.setText(str(user_data[2]))
                    
                    self.ui.new_zone_label.setText(str(user_data[3]))
                    self.ui.new_bay_label.setText(str(user_data[4]))
                    self.ui.new_lot_label.setText(str(user_data[5]))
                    self.ui.status_check_label1.setText("New lot already")
                else:
                    self.ui.status_check_label1.setText("New lot error")

                #update data on database
                user_id = user_data[0]
                update_new_lot_id = user_data[6]
                mycursor = mydb.cursor()
                value = (update_new_lot_id,user_id)
                updatedb =('''
                           UPDATE card SET lot_id = %s WHERE card_id=%s''')

                try:
                    mycursor.execute(updatedb, value)
                    mydb.commit()
                    self.ui.status_check_label1.setText("อัพเดทฐานข้อมูลสำเร็จ")
                except:
                    self.ui.status_check_label1.setText("อัพเดทฐานข้อมูลไม่สำเร็จ")
                # print("data after update :",user_data)
                user_data.clear()
                # print(user_data)

            elif wrong_zone=="2":
                
                if user_data[1] <= "190" and user_data[4] in z1:
                    random_bay = random.choice([bay for bay in bay_order if bay not in z1])
                    new_zone = z2[random_bay]
                    
                    random_lot = random.choice(nz[random_bay])
                    nz[random_bay].remove(random_lot)
                elif user_data[1] > "190" and user_data[4] in z1:
                    random_bay = random.choice([bay for bay in bay_order if bay not in z1])
                    new_zone = z2[random_bay]

                    random_lot = random.choice(oz[random_bay])
                    oz[random_bay].remove(random_lot)
                
                #replace_new zone,bay,lot in list user_data=[]
                user_data[3] = int(new_zone)
                user_data[4] = random_bay
                user_data[5] = random_lot

                old_lot_id = user_data[5]
                # print("ก่อนดึง db ใหม่ :",old_lot_id)

                mydb = mc.connect(
                host="localhost",
                user="root",
                password="",
                database="carlot")

                mycursor2 = mydb.cursor()
                mycursor2.execute('''
                                    SELECT lot_id FROM lot WHERE number=%s
                                    ''',(old_lot_id,))
                data_id = mycursor2.fetchone()

                user_data[6] = data_id[0]
                # print("ดึงมาใหม่รอบ 2 หลังจากดึง :",user_data)

                if user_data:
                    self.ui.new_card_id_label.setText(str(user_data[0]))
                    self.ui.new_height_label.setText(str(user_data[1]))
                    self.ui.new_license_p_label.setText(str(user_data[2]))
                    
                    self.ui.new_zone_label.setText(str(user_data[3]))
                    self.ui.new_bay_label.setText(str(user_data[4]))
                    self.ui.new_lot_label.setText(str(user_data[5]))
                    self.ui.status_check_label1.setText("ได้ช่องจอดใหม่เรียบร้อย")
                else:
                    self.ui.status_check_label1.setText("การรับช่องจอดมีปัญหา")
                
                #update data on database
                user_id = user_data[0]
                update_new_lot_id = user_data[6]
                mycursor = mydb.cursor()
                value = (update_new_lot_id,user_id)
                updatedb =('''
                           UPDATE card SET lot_id = %s WHERE card_id=%s''')

                try:
                    mycursor.execute(updatedb, value)
                    mydb.commit()
                    self.ui.status_check_label1.setText("อัพเดทฐานข้อมูลสำเร็จ")
                except:
                    self.ui.status_check_label1.setText("อัพเดทฐานข้อมูลไม่สำเร็จ")
                # print("data after update :",user_data)
                user_data.clear()
                # print(user_data)
        except:
            self.ui.status_check_label1.setText("Can't get new lot.")

    def clear_data(self):
        self.ui.lineEdit.clear()
        self.ui.wrong_zone_line_edit.clear()
        #left top
        self.ui.label_11.clear()
        self.ui.label_12.clear()
        self.ui.label_13.clear()
        #right top
        self.ui.new_card_id_label.clear()
        self.ui.new_height_label.clear()
        self.ui.new_license_p_label.clear()
        #left bottom
        self.ui.label_28.clear()
        self.ui.label_29.clear()
        self.ui.label_30.clear()
        #right bottom
        self.ui.new_bay_label.clear()
        self.ui.new_lot_label.clear()
        self.ui.new_zone_label.clear()
        #status
        self.ui.status_check_label1.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    style_file = QFile("stylechange.qss")
    style_file.open(QFile.ReadOnly | QFile.Text)
    style_stream = QTextStream(style_file)
    app.setStyleSheet(style_stream.readAll())
    
    bigwindow = MainBigWindow()
    bigwindow.show()
    
    sys.exit(app.exec())
    
