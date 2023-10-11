 def return_lot(self):
        id_no = self.ui.return_edit.text()
        data_to_return = []
        mycursor.execute('''SELECT card.card_id, card.status_id, card.user_height, card.user_license_plate, lot.parked_zone, bay.bay_name, lot.number, lot.lot_id
            FROM lot
            INNER JOIN card ON lot.lot_id = card.lot_id                  
            INNER JOIN bay ON lot.bay_id = bay.bay_id
            WHERE card_id=%s ''',(id_no,))
        old_data = mycursor.fetchone()
        for row in old_data:
            data_to_return.append(row)
        print("ข้อมูลที่จะคืน ที่ดึงจาก card id :",data_to_return)
        print(data_to_return[6])
        print(parked_lot)
        print(row)
        try:
            # Check if the lot number is in the list of parked_lot
            lot_no_list=data_to_return[6]
            if lot_no_list in parked_lot:
                for index, row in enumerate(parked_lot):
                    if row == 2:
                        # Construct and execute the SQL query to update the row
                        update_query = "UPDATE lot SET status_id = '1' WHERE number = %s"
                        mycursor.execute(update_query, (lot_no_list,), (id_no))
                        mydb.commit()
                        
                        # print("Update successful for lot number", id_no)

                        query_card = "UPDATE card SET lot_id = '0' WHERE lot_id = %s"
                        mycursor.execute(query_card, (id_no,))
                        mydb.commit()
                        
                        insert_history = "INSERT INTO history ( 'caed_id', 'height', 'license_plate') VALUES (%s,%s,%s) FROM "
                        val = (insert_history,)
                        break  # Exit the loop after the first successful update
                
                self.ui.return_status_label.setText("อัพเดตสถานะสำเร็จ")
            else:
                self.ui.return_status_label.setText("ไม่พบเลขล็อตที่ต้องการอัพเดต")
        except :
            self.ui.return_status_label.setText("อัพเดตสถานะไม่สำเร็จ")
