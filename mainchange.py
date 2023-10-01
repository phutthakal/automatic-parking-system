import sys
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
data=[]

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

# oz = over heigh zone
oz={"A":oha,"F":ohf,"C":ohc,"B":ohb,"G":ohg,"D":ohd,"H":ohh,"E":ohe}

z={"A":zone_order[0],"B":zone_order[0],"C":zone_order[1],"D":zone_order[1],"E":zone_order[1],"F":zone_order[1],"G":zone_order[1],"H":zone_order[1]}
z1={"A":zone_order[0],"B":zone_order[0]}
z2={"C":zone_order[1],"D":zone_order[1],"E":zone_order[1],"F":zone_order[1],"G":zone_order[1],"H":zone_order[1]}

mydb = mc.connect(
        host="localhost",
        user="root",
        password="",
        database="carlot"
    )


class MainBigWindow(QMainWindow):
    def __init__(self):
        super(MainBigWindow, self).__init__()

        self.ui = Ui_Change_Bay()
        self.ui.setupUi(self)
        # self.showFullScreen()
        
        #flamelesswindow
        # self.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
        self.ui.load_db_btn.clicked.connect(self.fetch_data)
        
    
    def load_data(self):
        try:
            mycursor = mydb.cursor()
            mycursor.execute("SELECT bay_name FROM bay")
            result = mycursor.fetchall()
            for row in result:
                bay_order.append(row[0])
            print(bay_order)

            mycursor.execute("SELECT number FROM lot WHERE status_id='1' AND bay_id='1'")
            result = mycursor.fetchall()
            for lot_a in result:
                a.append(lot_a[0])
            # print(a)

            mycursor.execute("SELECT number FROM lot WHERE status_id='1' AND bay_id='2'")
            result = mycursor.fetchall()
            for lot_a in result:
                b.append(lot_a[0])
            # print(b)

            mycursor.execute("SELECT number FROM lot WHERE status_id='1' AND bay_id='3'")
            result = mycursor.fetchall()
            for lot_a in result:
                c.append(lot_a[0])
            # print(c)

            mycursor.execute("SELECT number FROM lot WHERE status_id='1' AND bay_id='4'")
            result = mycursor.fetchall()
            for lot_a in result:
                d.append(lot_a[0])
            # print(d)

            mycursor.execute("SELECT number FROM lot WHERE status_id='1' AND bay_id='5'")
            result = mycursor.fetchall()
            for lot_a in result:
                e.append(lot_a[0])
            # print(e)

            mycursor.execute("SELECT number FROM lot WHERE status_id='1' AND bay_id='6'")
            result = mycursor.fetchall()
            for lot_a in result:
                f.append(lot_a[0])
            # print(f)

            mycursor.execute("SELECT number FROM lot WHERE status_id='1' AND bay_id='7'")
            result = mycursor.fetchall()
            for lot_a in result:
                g.append(lot_a[0])
            # print(g)

            mycursor.execute("SELECT number FROM lot WHERE status_id='1' AND bay_id='8'")
            result = mycursor.fetchall()
            for lot_a in result:
                h.append(lot_a[0])
            # print(h)
            self.ui.status_check_label.setText("Load complete")
        except:
            self.ui.status_check_label.setText("Load incomplete")

    def change_lot():
        try:
            db_cursor = mydb.cursor()
            db_cursor.execute("SELECT bay_name FROM bay")
            result = db_cursor.fetchall()
            for row in result:
                bay_order.append(row[0])
            print(bay_order)
            
            db_cursor.execute("SELECT number FROM lot WHERE number LIKE 'A%'")
            result = db_cursor.fetchall()
            for lot_a in result:
                a.append(lot_a[0])
            # print(a)
            db_cursor.execute("SELECT number FROM lot WHERE number LIKE 'B%'")
            result = db_cursor.fetchall()
            for lot_b in result:
                b.append(lot_b[0])
            # print(b)
            db_cursor.execute("SELECT number FROM lot WHERE number LIKE 'C%'")
            result = db_cursor.fetchall()
            for lot_c in result:
                c.append(lot_c[0])
            # print(c)
            db_cursor.execute("SELECT number FROM lot WHERE number LIKE 'D%'")
            result = db_cursor.fetchall()
            for lot_d in result:
                d.append(lot_d[0])
            # print(d)
            db_cursor.execute("SELECT number FROM lot WHERE number LIKE 'E%'")
            result = db_cursor.fetchall()
            for lot_e in result:
                e.append(lot_e[0])
            # print(e)
            db_cursor.execute("SELECT number FROM lot WHERE number LIKE 'F%'")
            result = db_cursor.fetchall()
            for lot_f in result:
                f.append(lot_f[0])
            # print(f)
            db_cursor.execute("SELECT number FROM lot WHERE number LIKE 'G%'")
            result = db_cursor.fetchall()
            for lot_g in result:
                g.append(lot_g[0])
            # print(g)
            db_cursor.execute("SELECT number FROM lot WHERE number LIKE 'H%'")
            result = db_cursor.fetchall()
            for lot_h in result:
                g.append(lot_h[0])
            

            list_input = input("Parking Bay: ")
            if list_input  in bay_order:
                bay_order.remove(list_input)
                bay_order.append(list_input)
                print(nz[list_input])
                        
                list_lot = input("Parking Lot: ")
                if list_lot not in parked_lot:
                    parked_lot.append(list_lot)
                    nz[list_input].remove(list_lot)
                    print("Zone :",z[list_input])
                    print("Bay: ", list_input)
                    print("Lot: ", parked_lot)

            if list_input in bay_order:
                bay_order.remove(list_input)
                bay_order.append(list_input)
                print("********************************************")
                print("Parking Zone: ",z[list_input])
                print("Parking Bay: ", bay_order[7])
                print("Parking Lot: ", parked_lot)
                list_a = input("Want to change Bay y/n: ")
                print("***********************************************")
                
                if list_a == "y":
                    parked_lot.clear()
                    random_bay = random.choice(bay_order)
                    random_lot = random.choice(nz[random_bay])
                    nz[random_bay].remove(random_lot)
                    selected_zone = z[random_bay]
                    print("Bay: ",random_bay)
                    print("Lot: ",random_lot)
                    print("Zone: ",selected_zone)

                else:
                    print("Thank you.")
            else:
                print("Invalid bay selected.")
        except:
            print("Error.")

    def fetch_data(self):
        card_id = self.ui.lineEdit.text()
        wrong_bay = self.ui.lineEdit_2.text()
        
        try:
            mydb = mc.connect(
                host="localhost",
                user="root",
                password="",
                database="carlot"
            )
            # mycursor = mydb.cursor()
            # mycursor.execute("SELECT card_id, user_height, user_license_plate FROM card WHERE card_id=%s",(card_id,))
            # data1 = mycursor.fetchone()

            mycursor2 = mydb.cursor()
            # mycursor2.execute("""
            #     SELECT lot.number, bay.bay_name, lot.parked_zone, card.card_id, card.user_height, card.user_license_plate, lot.lot_id
            #     FROM lot
            #     INNER JOIN card ON lot.lot_id = card.lot_id
            #     INNER JOIN bay ON lot.bay_id = bay.bay_name
            #     WHERE card.card_id=%s
            # """, (card_id,))
            mycursor2.execute('''
            SELECT card.card_id, card.user_height, card.user_license_plate, lot.parked_zone, bay.bay_name, lot.number
            FROM lot
            INNER JOIN card ON lot.lot_id = card.lot_id                  
            INNER JOIN bay ON lot.bay_id = bay.bay_id
            WHERE card_id=%s
            ''', (card_id,))
            data = mycursor2.fetchone()
                
            if data:
                self.ui.label_11.setText(str(data[0]))
                self.ui.label_12.setText(str(data[1]))
                self.ui.label_13.setText(str(data[2]))
                
                self.ui.label_28.setText(str(data[3]))
                self.ui.label_29.setText(str(data[4]))
                self.ui.label_30.setText(str(data[5]))
                self.ui.status_check_label.setText("Fetch DB Complete")
                print(data)
            else:
                self.ui.status_check_label.setText("card ID not found")


        except:
            self.ui.status_check_label.setText("Fetch data Error")



if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    style_file = QFile("stylechange.qss")
    style_file.open(QFile.ReadOnly | QFile.Text)
    style_stream = QTextStream(style_file)
    app.setStyleSheet(style_stream.readAll())
    
    bigwindow = MainBigWindow()
    bigwindow.show()
     
    sys.exit(app.exec())
'''

'''
    
