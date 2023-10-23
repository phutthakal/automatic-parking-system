import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget
from PyQt5.QtCore import pyqtSlot, QFile, QTextStream
import mysql.connector as mc
import requests
import datetime

from Mainwindow_final import Ui_MainWindow
from mainbig import *
from mainsmall import *
from mainchange import *

# bay_order=["A","F","C","B","G","D","H","E"]
bay_order=[]
zone_order=["1","2"]
parked_lot=[]


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

mydb = mc.connect(
        host="localhost",
        user="root",
        password="",
        database="carlot"
    )

#load bay order 
mycursor = mydb.cursor()
mycursor.execute('''SELECT name FROM bay_order WHERE status='5' ''')
present_order = mycursor.fetchall()
for row in present_order:
    bay_order.append(row[0])
# print("check present",bay_order)

#bay_a : bay_id='1'
mycursor = mydb.cursor()
mycursor.execute("SELECT number FROM lot WHERE status_id='1' AND bay_id='1' AND parking_type_id='0'")
normal_zone_result=mycursor.fetchall()
for row in normal_zone_result:
    a.append(row[0])
    
mycursor.execute("SELECT number FROM lot WHERE status_id='1' AND bay_id='1' AND parking_type_id='1'")
over_zone_result = mycursor.fetchall()
for row in over_zone_result:
    oha.append(row[0])
    
#bay_b : bay_id='2'
mycursor.execute("SELECT number FROM lot WHERE status_id='1' AND bay_id='2' AND parking_type_id='0'")
normal_zone_result=mycursor.fetchall()
for row in normal_zone_result:
    b.append(row[0])

mycursor.execute("SELECT number FROM lot WHERE status_id='1' AND bay_id='2' AND parking_type_id='1'")
over_zone_result = mycursor.fetchall()
for row in over_zone_result:
    ohb.append(row[0])

#bay_c : bay_id='3'
mycursor.execute("SELECT number FROM lot WHERE status_id='1' AND bay_id='3' AND parking_type_id='0'")
normal_zone_result=mycursor.fetchall()
for row in normal_zone_result:
    c.append(row[0])

mycursor.execute("SELECT number FROM lot WHERE status_id='1' AND bay_id='3' AND parking_type_id='1'")
over_zone_result = mycursor.fetchall()
for row in over_zone_result:
    ohc.append(row[0])

#bay_d : bay_id='4'
mycursor.execute("SELECT number FROM lot WHERE status_id='1' AND bay_id='4' AND parking_type_id='0'")
normal_zone_result=mycursor.fetchall()
for row in normal_zone_result:
    d.append(row[0])

mycursor.execute("SELECT number FROM lot WHERE status_id='1' AND bay_id='4' AND parking_type_id='1'")
over_zone_result = mycursor.fetchall()
for row in over_zone_result:
    ohd.append(row[0])

#bay_e : bay_id='5'
mycursor.execute("SELECT number FROM lot WHERE status_id='1' AND bay_id='5' AND parking_type_id='0'")
normal_zone_result=mycursor.fetchall()
for row in normal_zone_result:
    e.append(row[0])

mycursor.execute("SELECT number FROM lot WHERE status_id='1' AND bay_id='5' AND parking_type_id='1'")
over_zone_result = mycursor.fetchall()
for row in over_zone_result:
    ohe.append(row[0])

#bay_f : bay_id='6'
mycursor.execute("SELECT number FROM lot WHERE status_id='1' AND bay_id='6' AND parking_type_id='0'")
normal_zone_result=mycursor.fetchall()
for row in normal_zone_result:
    f.append(row[0])

mycursor.execute("SELECT number FROM lot WHERE status_id='1' AND bay_id='6' AND parking_type_id='1'")
over_zone_result = mycursor.fetchall()
for row in over_zone_result:
    ohf.append(row[0])

#bay_g : bay_id='7'
mycursor.execute("SELECT number FROM lot WHERE status_id='1' AND bay_id='7' AND parking_type_id='0'")
normal_zone_result=mycursor.fetchall()
for row in normal_zone_result:
    g.append(row[0])

mycursor.execute("SELECT number FROM lot WHERE status_id='1' AND bay_id='7' AND parking_type_id='1'")
over_zone_result = mycursor.fetchall()
for row in over_zone_result:
    ohg.append(row[0])

#bay_h : bay_id='8'
mycursor.execute("SELECT number FROM lot WHERE status_id='1' AND bay_id='8' AND parking_type_id='0'")
normal_zone_result=mycursor.fetchall()
for row in normal_zone_result:
    h.append(row[0])

mycursor.execute("SELECT number FROM lot WHERE status_id='1' AND bay_id='8' AND parking_type_id='1'")
over_zone_result = mycursor.fetchall()
for row in over_zone_result:
    ohh.append(row[0])

mycursor.execute('''SELECT number,status_id FROM lot WHERE status_id=7 ''')
old_return_data = mycursor.fetchall()
for row in old_return_data:
    parked_lot.append(row[1])
    parked_lot.append(row[0])
# print("information before return :",parked_lot)

# nz = normal zone
nz={"A":a,"F":f,"C":c,"B":b,"G":g,"D":d,"H":h,"E":e}

# oz = over heigh zone
oz={"A":oha,"F":ohf,"C":ohc,"B":ohb,"G":ohg,"D":ohd,"H":ohh,"E":ohe}

#Parking Zone
z={"A":zone_order[0],"B":zone_order[0],"C":zone_order[1],"D":zone_order[1],"E":zone_order[1],"F":zone_order[1],"G":zone_order[1],"H":zone_order[1]}


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.icon_only_widget.hide()
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.full_accept_btn.setChecked(True)
        self.ui.stacked_bay.setCurrentIndex(0)
        self.ui.locasort_a_btn.setChecked(True)
        self.ui.monitor1_btn.clicked.connect(self.smallscreen)
        self.ui.monitor2_btn.clicked.connect(self.bigscreen)
        # self.ui.reload_btn.clicked.connect(self.load_data_api)
        self.ui.accept_btn.clicked.connect(self.get_lot)
        self.ui.return_btn.clicked.connect(self.return_lot)
        self.ui.load_change_sw_btn.clicked.connect(self.changescreen)
        self.ui.locasort_a_btn.clicked.connect(self.check_full_lot)
        self.ui.locasort_b_btn.clicked.connect(self.check_full_lot)
        self.ui.locasort_c_btn.clicked.connect(self.check_full_lot)
        self.ui.locasort_d_btn.clicked.connect(self.check_full_lot)
        self.ui.locasort_e_btn.clicked.connect(self.check_full_lot)
        self.ui.locasort_f_btn.clicked.connect(self.check_full_lot)
        self.ui.locasort_g_btn.clicked.connect(self.check_full_lot)
        self.ui.locasort_h_btn.clicked.connect(self.check_full_lot)
        self.ui.clear_accept_db_btn.clicked.connect(self.clear_accept)
        self.ui.clear_return_db_btn.clicked.connect(self.clear_return)


    def on_icon_accept_btn_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(0)

    def on_full_accept_btn_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(0)

    def on_icon_edit_btn_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(1)

    def on_full_edit_btn_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(1)

    def on_icon_monitor_btn_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(2)

    def on_full_monitor_btn_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(2)
        
    def on_locationsort_btn_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(3)

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


    def smallscreen(self):
        self.window = MainSmallWindow()    
        self.window.show()
    
    def bigscreen(self):
        self.mainbig = MainBigWindow()
        self.mainbig.show()

    def changescreen(self):
        self.changewindow = MainchangeWindow()
        self.changewindow.show()
    
    # def load_data_api(self):
    #     # response = requests.get('http://127.0.0.1:8000/api/test/users')
    #     response = requests.get('http://127.0.0.1:8000/cars/1')
    #     # api_card_id = response.json()[0]['license_plate']
    #     api_noplate = response.json()['license_plate']
    #     # api_height = str(response.json()['height'])
    #     height=(199,180)
    #     api_height = random.choice(height)
    #     self.ui.api_lcp_label.setText(api_noplate)
    #     self.ui.api_height_label.setText(str(api_height))
            
    def get_lot(self):
        data_api = []
        response = requests.get('http://127.0.0.1:8000/cars/1')
        api_noplate = str(response.json()['license_plate'])
        height=(199,180)
        api_height = random.choice(height)

        # api_height = int(response.json()['height'])
        data_api.append(api_noplate)
        data_api.append(api_height)
        # print("data from api now in list:",data_api)
        print(data_api)
        print(oz)
        print(nz)
        

        car_height = int(data_api[1])
        parking_lot = None
        # print(car_height)
        while True:
            for _ in range(8):
                if car_height >= 190:
                    removed_element = bay_order.pop(0)
                    bay_order.append(removed_element)

                    # ตรวจสอบ normal zone ถ้าเต็มให้ใช้ over zone แทน
                    # if len(oz[removed_element]) == 0:
                    #     continue
                    if len(oz[removed_element]) == 0:
                        if len(nz[removed_element]) == 0:
                            continue
                        else:
                            parking_lot = nz[removed_element].pop(0)
                    else:
                        parking_lot = oz[removed_element].pop(0)

                    # parking_lot = oz[removed_element].pop(0)
                    parked_lot.append(parking_lot)

                    self.ui.accept_show_zone_label.setText(z[removed_element[0]])
                    self.ui.accept_show_bay_label.setText(removed_element)
                    self.ui.accept_show_lot_label.setText(parking_lot)

                    lot_ready_to_db = parking_lot

                    old_lot_id = []
                    mycursor = mydb.cursor()
                    mycursor.execute('''SELECT lot_id FROM lot WHERE number = %s''', (lot_ready_to_db,))
                    old_data = mycursor.fetchone()
                    for row in old_data:
                        old_lot_id.append(row)

                    value = (old_data)
                    updatedb = '''UPDATE lot SET status_id = "6" WHERE lot_id = %s'''
                    try:
                        mycursor.execute(updatedb, value)
                        mydb.commit()
                        self.ui.accept_status_label.setText("บันทึกสำเร็จ")
                    except:
                        self.ui.accept_status_label.setText("บันทึกไม่สำเร็จ")

                    card_id = self.ui.lineEdit.text()
                    id_now = old_data[0]
                    value2 = (id_now, card_id)
                    updatedb2 = '''UPDATE card SET lot_id = %s, status_id = "3" WHERE card_id = %s'''
                    try:
                        mycursor.execute(updatedb2, value2)
                        mydb.commit()
                        self.ui.accept_status_label.setText("บันทึกลงการ์ดสำเร็จ")
                    except:
                        self.ui.accept_status_label.setText("บันทึกลงการ์ดไม่สำเร็จ")

                    license_plate_ready_to_get_lot = data_api[0]
                    height_plate_ready_to_get_lot = data_api[1]

                    value3 = (height_plate_ready_to_get_lot, license_plate_ready_to_get_lot, card_id)
                    updatedb3 = '''UPDATE card SET user_height = %s, user_license_plate = %s WHERE card_id = %s'''
                    mycursor.execute(updatedb3, value3)
                    mydb.commit()

                    data_to_insert_history = []

                    mycursor = mydb.cursor()
                    mycursor.execute('''
                        SELECT card.card_id, card.user_height, card.user_license_plate, lot.lot_id, card.time, lot.number
                        FROM lot
                        INNER JOIN card ON lot.lot_id = card.lot_id
                        WHERE lot.number = %s
                    ''', (lot_ready_to_db,))

                    card_data_to_history = mycursor.fetchall()

                    for row in card_data_to_history:
                        data_to_insert_history.append(row)

                    for data_row in data_to_insert_history:
                        card_id_in_list = data_row[0]
                        height_in_list = data_row[1]
                        lp_in_list = data_row[2]
                        lot_id_in_list = data_row[3]
                        timestamp_in_list = data_row[4]
                        mycursor.execute('''
                            INSERT INTO history
                            (his_id, card_id, height, license_plate, lot_id, time_in, time_out)
                            VALUES (NULL, %s, %s, %s, %s, %s, NULL)
                        ''', (card_id_in_list, height_in_list, lp_in_list, lot_id_in_list, timestamp_in_list))

                    mydb.commit()
                    return parked_lot
                else:
                    removed_element = bay_order.pop(0)            
                    bay_order.append(removed_element)

                    # if len(nz[removed_element])==0:
                    #     continue
                    # parking_lot = nz[removed_element].pop(0)
                    if len(nz[removed_element]) == 0:
                        if len(oz[removed_element]) == 0:
                            continue
                        else:
                            parking_lot = oz[removed_element].pop(0)
                    else:
                        parking_lot = nz[removed_element].pop(0)

                    parked_lot.append(parking_lot)
                    
                    self.ui.accept_show_zone_label.setText(z[removed_element[0]])
                    self.ui.accept_show_bay_label.setText(removed_element)
                    self.ui.accept_show_lot_label.setText(parking_lot)

                    #Element to use
                    lot_ready_to_db = parking_lot
                    # print(lot_ready_to_db)

                    old_lot_id = []
                    mycursor = mydb.cursor()
                    mycursor.execute('''
                                        SELECT lot_id FROM lot WHERE number=%s
                                        ''',(lot_ready_to_db,))
                    old_data = mycursor.fetchone()
                    for row in old_data:
                        old_lot_id.append(row)
                    # print('lot id :',old_lot_id)

                    #update lot status_id by lot_id from (old_data = mycursor.fetchone())
                    value = (old_data)
                    updatedb = ('''UPDATE lot SET status_id="6" WHERE lot_id=%s ''')
                    try:
                        mycursor.execute(updatedb, value)
                        mydb.commit()
                        self.ui.accept_status_label.setText("บันทึกสำเร็จ")
                    except:
                        self.ui.accept_status_label.setText("บันทึกไม่สำเร็จ")

                     #อัพเดตข้อมูลช่องจอดลงใน card โดยล็อค card id
                    card_id = self.ui.lineEdit.text()
                    id_now = old_data[0]
                    value2 = (id_now, card_id)
                    updatedb2 =('''UPDATE card SET lot_id=%s, status_id="3" WHERE card_id=%s ''')
                    try:
                        mycursor.execute(updatedb2, value2)
                        mydb.commit()
                        self.ui.accept_status_label.setText("บันทึกลงการ์ดสำเร็จ")
                    except:
                        self.ui.accept_status_label.setText("บันทึกลงการ์ดไม่สำเร็จ")
                    
                    licese_plate_ready_to_get_lot = data_api[0]
                    height_plate_ready_to_get_lot = data_api[1]

                    value3 = (height_plate_ready_to_get_lot, licese_plate_ready_to_get_lot,  card_id)
                    updatedb3 =('''UPDATE card SET user_height=%s,user_license_plate=%s WHERE card_id=%s ''')
                    mycursor.execute(updatedb3, value3)
                    mydb.commit()

                    #insert_data to history table
                    data_to_insert_history = []

                    # print("ข้อมูลช่องจอด:", parked_lot)

                    mycursor = mydb.cursor()
                    mycursor.execute('''
                        SELECT card.card_id, card.user_height, card.user_license_plate, lot.lot_id, card.time, lot.number
                        FROM lot
                        INNER JOIN card ON lot.lot_id = card.lot_id 
                        WHERE lot.number = %s
                    ''', (lot_ready_to_db,))

                    card_data_to_history = mycursor.fetchall()

                    for row in card_data_to_history:
                        data_to_insert_history.append(row)

                    # print("data fetch", data_to_insert_history)

                    #insert time in
                    for data_row in data_to_insert_history:
                        card_id_in_list = data_row[0]
                        height_in_list = data_row[1]
                        lp_in_list = data_row[2]
                        lot_id_in_list = data_row[3]
                        timestamp_in_list = data_row[4]
                        mycursor.execute('''
                            INSERT INTO history 
                            (his_id, card_id, height, license_plate, lot_id, time_in, time_out) 
                            VALUES (NULL, %s, %s, %s, %s, %s, NULL)
                        ''', (card_id_in_list, height_in_list, lp_in_list, lot_id_in_list, timestamp_in_list))

                    mydb.commit()
                    return parked_lot
            return parking_lot

    
    def return_lot(self):
        id_no = self.ui.return_edit.text()

        mycursor = mydb.cursor()
        mycursor.execute('''SELECT card.card_id, card.status_id, card.user_height, card.user_license_plate, lot.parked_zone, bay.bay_name, lot.number, lot.lot_id
            FROM lot
            INNER JOIN card ON lot.lot_id = card.lot_id                  
            INNER JOIN bay ON lot.bay_id = bay.bay_id
            WHERE card_id=%s ''', (id_no,))
        
        old_data = mycursor.fetchone()

        if old_data:
            card_id, status_id, user_height, user_license_plate, parked_zone, bay_name, number, lot_id = old_data

            # print("ข้อมูลที่จะคืน ที่ดึงจาก card id :", old_data)

            # Check if the lot number is in the list of parked_lot
            lot_no_list = number
            if lot_no_list in parked_lot:
                # Construct and execute the SQL query to update the row for 'lot' table
                update_query_lot = "UPDATE lot SET status_id = '1' WHERE number = %s"
                mycursor.execute(update_query_lot, (lot_no_list,))
                mydb.commit()

                # Construct and execute the SQL query to update the row for 'card' table
                update_query_card = "UPDATE card SET lot_id=%s, status_id='1' WHERE lot_id=%s"
                mycursor.execute(update_query_card, (None, lot_id))  # Assuming None means no lot assigned
                mydb.commit()

                # Insert time_out into history table
                mycursor.execute('''SELECT time FROM card WHERE card_id=%s''', (id_no,))
                card_time_out = mycursor.fetchone()

                if card_time_out:
                    # ดึงเวลาปัจจุบัน
                    current_time_out = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

                    # ปรับปรุงข้อมูลเวลาออกในตาราง history
                    mycursor.execute('''UPDATE history 
                                        SET time_out = %s 
                                        WHERE card_id = %s AND time_out IS NULL''', (current_time_out, id_no))
                    mydb.commit()

                # print("ข้อมูล lot หลังดึงข้อมูล:", current_time_out)
                self.ui.return_status_label.setText("คืนเรียบร้อย")
            else:
                print("Lot number not found in parked_lot list.")
        else:
            print("Card ID not found in the database.")


    def clear_accept(self):
        self.ui.lineEdit.clear()
        self.ui.accept_show_zone_label.clear()
        self.ui.accept_show_bay_label.clear()
        self.ui.accept_show_lot_label.clear()
        self.ui.accept_status_label.clear()
        self.ui.api_lcp_label.clear()
        self.ui.api_height_label.clear()

    def clear_return(self):
        self.ui.return_edit.clear()
        self.ui.return_status_label.clear()

    def check_full_lot(self):
        while True:
            list=[]
            mycursor = mydb.cursor()
            mycursor.execute("SELECT number,status_id FROM lot  ")
            lot_db = mycursor.fetchall()
        
            for row in lot_db:
                list.append(row[1])
            # print(list)
            # สร้างลิสต์ของ label
            labels = [self.ui.label_a101, self.ui.label_a102, self.ui.label_a103, self.ui.label_a104,
                    self.ui.label_a201, self.ui.label_a202, self.ui.label_a203, self.ui.label_a204,
                    self.ui.label_a301, self.ui.label_a302, self.ui.label_a303, self.ui.label_a304,
                    self.ui.label_a401, self.ui.label_a402, self.ui.label_a403, self.ui.label_a404,
                    self.ui.label_a501, self.ui.label_a502, self.ui.label_a503, self.ui.label_a504,
                    self.ui.label_a601, self.ui.label_a602, self.ui.label_a603, self.ui.label_a604,
                    self.ui.label_a701, self.ui.label_a702, self.ui.label_a703, self.ui.label_a704,
                    self.ui.label_a705 ,
                    
                    self.ui.label_b101, self.ui.label_b102, self.ui.label_b103, self.ui.label_b104,
                    self.ui.label_b201, self.ui.label_b202, self.ui.label_b203, self.ui.label_b204,
                    self.ui.label_b301, self.ui.label_b302, self.ui.label_b303, self.ui.label_b304,
                    self.ui.label_b401, self.ui.label_b402, self.ui.label_b403, self.ui.label_b404,
                    self.ui.label_b501, self.ui.label_b502, self.ui.label_b503, self.ui.label_b504,
                    self.ui.label_b601, self.ui.label_b602, self.ui.label_b603, self.ui.label_b604,
                    self.ui.label_b701, self.ui.label_b702, self.ui.label_b703, self.ui.label_b704,
                    self.ui.label_b705,
                    self.ui.label_c101, self.ui.label_c102, self.ui.label_c103, self.ui.label_c104,
                    self.ui.label_c201, self.ui.label_c202, self.ui.label_c203, self.ui.label_c204,
                    self.ui.label_c301, self.ui.label_c302, self.ui.label_c303, self.ui.label_c304,
                    self.ui.label_c401, self.ui.label_c402, self.ui.label_c403, self.ui.label_c404,
                    self.ui.label_c501, self.ui.label_c502, self.ui.label_c503, self.ui.label_c504,
                    self.ui.label_c601, self.ui.label_c602, self.ui.label_c603, self.ui.label_c604,
                    self.ui.label_c701, self.ui.label_c702, self.ui.label_c703, self.ui.label_c704,
                    self.ui.label_c705,
                    self.ui.label_d101, self.ui.label_d102, self.ui.label_d103, self.ui.label_d104,
                    self.ui.label_d201, self.ui.label_d202, self.ui.label_d203, self.ui.label_d204,
                    self.ui.label_d301, self.ui.label_d302, self.ui.label_d303, self.ui.label_d304,
                    self.ui.label_d401, self.ui.label_d402, self.ui.label_d403, self.ui.label_d404,
                    self.ui.label_d501, self.ui.label_d502, self.ui.label_d503, self.ui.label_d504,
                    self.ui.label_d601, self.ui.label_d602, self.ui.label_d603, self.ui.label_d604,
                    self.ui.label_d701, self.ui.label_d702, self.ui.label_d703, self.ui.label_d704,
                    self.ui.label_d705,
                    self.ui.label_e101, self.ui.label_e102, self.ui.label_e103, self.ui.label_e104,
                    self.ui.label_e201, self.ui.label_e202, self.ui.label_e203, self.ui.label_e204,
                    self.ui.label_e301, self.ui.label_e302, self.ui.label_e303, self.ui.label_e304,
                    self.ui.label_e401, self.ui.label_e402, self.ui.label_e403, self.ui.label_e404,
                    self.ui.label_e501, self.ui.label_e502, self.ui.label_e503, self.ui.label_e504,
                    self.ui.label_e601, self.ui.label_e602, self.ui.label_e603, self.ui.label_e604,
                    self.ui.label_e701, self.ui.label_e702, self.ui.label_e703, self.ui.label_e704,
                    self.ui.label_e705,
                    self.ui.label_f101, self.ui.label_f102, self.ui.label_f103, self.ui.label_f104,
                    self.ui.label_f201, self.ui.label_f202, self.ui.label_f203, self.ui.label_f204,
                    self.ui.label_f301, self.ui.label_f302, self.ui.label_f303, self.ui.label_f304,
                    self.ui.label_f401, self.ui.label_f402, self.ui.label_f403, self.ui.label_f404,
                    self.ui.label_f501, self.ui.label_f502, self.ui.label_f503, self.ui.label_f504,
                    self.ui.label_f601, self.ui.label_f602, self.ui.label_f603, self.ui.label_f604,
                    self.ui.label_f701, self.ui.label_f702, self.ui.label_f703, self.ui.label_f704,
                    self.ui.label_f705,
                    self.ui.label_g101, self.ui.label_g102, self.ui.label_g103, self.ui.label_g104,
                    self.ui.label_g201, self.ui.label_g202, self.ui.label_g203, self.ui.label_g204,
                    self.ui.label_g301, self.ui.label_g302, self.ui.label_g303, self.ui.label_g304,
                    self.ui.label_g401, self.ui.label_g402, self.ui.label_g403, self.ui.label_g404,
                    self.ui.label_g501, self.ui.label_g502, self.ui.label_g503, self.ui.label_g504,
                    self.ui.label_g601, self.ui.label_g602, self.ui.label_g603, self.ui.label_g604,
                    self.ui.label_g701, self.ui.label_g702, self.ui.label_g703, self.ui.label_g704,
                    self.ui.label_g705,

                    self.ui.label_h101, self.ui.label_h102, self.ui.label_h103, self.ui.label_h104,
                    self.ui.label_h201, self.ui.label_h202, self.ui.label_h203, self.ui.label_h204,
                    self.ui.label_h301, self.ui.label_h302, self.ui.label_h303, self.ui.label_h304,
                    self.ui.label_h401, self.ui.label_h402, self.ui.label_h403, self.ui.label_h404,
                    self.ui.label_h501, self.ui.label_h502, self.ui.label_h503, self.ui.label_h504,
                    self.ui.label_h601, self.ui.label_h602, self.ui.label_h603, self.ui.label_h604,
                    self.ui.label_h701, self.ui.label_h702, self.ui.label_h703, self.ui.label_h704,
                    self.ui.label_h705 
                    ]

            for item, label in zip(list, labels):
                if item == 7:
                    label.setStyleSheet("background-color: #580EF6;border-radius: 10px;")
                else:
                    label.setStyleSheet("background-color: #fff;border-radius: 10px;")
                           
            break


if __name__ == "__main__":
    app = QApplication(sys.argv)

    style_file = QFile("style_final.qss")
    style_file.open(QFile.ReadOnly | QFile.Text)
    style_stream = QTextStream(style_file)
    app.setStyleSheet(style_stream.readAll())

    window = MainWindow()
    window.show()

    sys.exit(app.exec())

