import mysql.connector
import random
#ทำการเชื่อมต่อกับฐานข้อมูลง่าย ๆ แค่ใส่ Host / User / Password ให้ถูกต้อง
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="parking system"
             )

bay_order=[]
parked_lot=[]
zone_order=['1','2']

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

# import mysql.connector
# #ทำการเชื่อมต่อกับฐานข้อมูลง่าย ๆ แค่ใส่ Host / User / Password ให้ถูกต้อง
# connection = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="",
#     database="parking system"
#              )
# db_cursor = connection.cursor()
# # db_cursor.execute("SELECT bay FROM parking_bay WHERE status='empty'")
# # result = db_cursor.fetchall()
# # for row in result:
# #     print(row[0])


try:
    db_cursor = connection.cursor()
    db_cursor.execute("SELECT bay FROM parking_bay WHERE status='empty'")
    result = db_cursor.fetchall()
    for row in result:
        bay_order.append(row[0])
    print(bay_order)
    db_cursor = connection.cursor()
    db_cursor.execute("SELECT lot FROM parking_lot WHERE lot LIKE 'A%'")
    result = db_cursor.fetchall()
    for lot_a in result:
        a.append(lot_a[0])
    # print(a)
    db_cursor.execute("SELECT lot FROM parking_lot WHERE lot LIKE 'B%'")
    result = db_cursor.fetchall()
    for lot_b in result:
        b.append(lot_b[0])
    # print(b)
    db_cursor.execute("SELECT lot FROM parking_lot WHERE lot LIKE 'C%'")
    result = db_cursor.fetchall()
    for lot_c in result:
        c.append(lot_c[0])
    # print(c)
    db_cursor.execute("SELECT lot FROM parking_lot WHERE lot LIKE 'D%'")
    result = db_cursor.fetchall()
    for lot_d in result:
        d.append(lot_d[0])
    # print(d)
    db_cursor.execute("SELECT lot FROM parking_lot WHERE lot LIKE 'E%'")
    result = db_cursor.fetchall()
    for lot_e in result:
        e.append(lot_e[0])
    # print(e)
    db_cursor.execute("SELECT lot FROM parking_lot WHERE lot LIKE 'F%'")
    result = db_cursor.fetchall()
    for lot_f in result:
        f.append(lot_f[0])
    # print(f)
    db_cursor.execute("SELECT lot FROM parking_lot WHERE lot LIKE 'G%'")
    result = db_cursor.fetchall()
    for lot_g in result:
        g.append(lot_g[0])
    # print(g)
    db_cursor.execute("SELECT lot FROM parking_lot WHERE lot LIKE 'H%'")
    result = db_cursor.fetchall()
    for lot_h in result:
        g.append(lot_h[0])
    # print(h)
    # db_cursor.execute("SELECT zone FROM zone ")
    # result = db_cursor.fetchall()
    # for zone in result:
    #     zone_order.append(zone[0])
    # print(zone_order)

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
