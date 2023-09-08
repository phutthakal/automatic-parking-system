import ast
import mysql.connector as mc

a=[]

oha=[]

mydb = mc.connect(
        host="localhost",
        user="root",
        password="",
        database="carlot"
    )
mycursor = mydb.cursor()
mycursor.execute("SELECT number FROM lot WHERE parking_zone_id='0' AND status_id='1' ")
normal_zone_result=mycursor.fetchall()
a.append(normal_zone_result)
# normal_zone_result = [item[0] for item in ast.literal_eval(str(normal_zone_item))]



# mycursor2 = mydb.cursor()
# mycursor2.execute("SELECT number FROM lot WHERE parking_zone_id='1' AND status_id='1'")
# over_zone_result = mycursor2.fetchall()

# oha.append(str(over_zone_result))

print("normal zone :",a)
print("over zone :",oha)
