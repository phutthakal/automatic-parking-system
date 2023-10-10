#update lot status
                update_new_lot_id = data_id
                value2 = (update_new_lot_id)
                updatedb2 =('''
                           UPDATE lot SET status_id="3" WHERE lot_id=%s ''')
                try:
                    mycursor.execute(updatedb2, value2)
                    mydb.commit()
                    self.ui.status_check_label1.setText("อัพเดทฐานข้อมูลสำเร็จ")
                except:
                    self.ui.status_check_label1.setText("อัพเดทฐานข้อมูลไม่สำเร็จ")
