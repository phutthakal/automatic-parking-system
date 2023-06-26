bay_order=["A","F","C","B","G","D","H","E"]
avaliable_lot=[]

a=["A201","A202","A203","A204",
   "A301","A302","A303","A304",
   "A401","A402","A403","A404",
   "A501","A502","A503","A504",
   "A601","A602","A603","A604",
   "A701","A702","A703","A704","A705"]
b=["B201","B202","B203","B204",
   "B301","B302","B303","B304",
   "B401","B402","B403","B404",
   "B501","B502","B503","B504",
   "B601","B602","B603","B604",
   "B701","B702","B703","B704","B705"]
c=["C201","C202","C203","C204",
   "C301","C302","C303","C304",
   "C401","C402","C403","C404",
   "C501","C502","C503","C504",
   "C601","C602","C603","C604",
   "C701","C702","C703","C704","C705"]
d=["D201","D202","D203","D204",
   "D301","D302","D303","D304",
   "D401","D402","D403","D404",
   "D501","D502","D503","D504",
   "D601","D602","D603","D604",
   "D701","D702","D703","D704","D705"]
e=["E201","E202","E203","E204",
   "E301","E302","E303","E304",
   "E401","E402","E403","E404",
   "E501","E502","E503","E504",
   "E601","E602","E603","E604",
   "E701","E702","E703","E704","E705"]
f=["F201","F202","F203","F204",
   "F301","F302","F303","F304",
   "F401","F402","F403","F404",
   "F501","F502","F503","F504",
   "F601","F602","F603","F604",
   "F701","F702","F703","F704","F705"]
g=["G201","G202","G203","G204",
   "G301","G302","G303","G304",
   "G401","G402","G403","G404",
   "G501","G502","G503","G504",
   "G601","G602","G603","G604",
   "G701","G702","G703","G704","G705"]
h=["H201","H202","H203","H204",
   "H301","H302","H303","H304",
   "H401","H402","H403","H404",
   "H501","H502","H503","H504",
   "H601","H602","H603","H604",
   "H701","H702","H703","H704","H705"]

oha=["A101","A102"]
ohb=["B101","B102"]
ohc=["C101","C102"]
ohd=["D101","D102"]
ohe=["E101","E102"]
ohf=["F101","F102"]
ohg=["G101","G102"]
ohh=["H101","H102"]

# nz = normal zone
nz={"A":a,"F":f,"C":c,"B":b,"G":g,"D":d,"H":h,"E":e}

# oz = over heigh zone
oz={"A":oha,"F":ohf,"C":ohc,"B":ohb,"G":ohg,"D":ohd,"H":ohh,"E":ohe}


def get_lot():
   while True:
      print("=====================================")
      user_height =int(input("Enter 'n' to select option\nInput your car height  : "))
      print("=====================================")
      if user_height=="":
         print("----- Enter your car height -----")
                                       
      elif user_height>=190:
         removed_element = bay_order.pop(0)
         bay_order.append(removed_element)
         remove_lot = oz[removed_element].pop(0)
         avaliable_lot.append(remove_lot)
         print("Your bay is :",removed_element)
         print("your parking lot is : ",remove_lot)
         print("avaliable lot check:",avaliable_lot)
         
         empty_lot = None
         for bay in bay_order:
            if len(oz[bay]) != 0:
               empty_lot = bay
               break
         if empty_lot is not None:
            # print("Found empty lot:", empty_lot)
            remove = oz[removed_element].pop(0)
            avaliable_lot.append(remove_lot)
            print("Your bay is :",empty_lot)
            print("your parking lot is : ",remove)
            print("avaliable lot check:",avaliable_lot)
         else:
            print("No empty lots available")

         
         
      elif user_height<190:
         removed_element = bay_order.pop(0)            
         bay_order.append(removed_element)                              
         print("Your bay is :",removed_element)
         remove_lot = nz[removed_element].pop(0)
         avaliable_lot.append(remove_lot)

         print("your parking lot is : ",remove_lot)
         print("Empty normal lot now : ",nz[removed_element])

      else:
         print("----- Enter valid car weight -----")




def return_lot():
    while True:
         print("-------------------------------")
         print("Avaliable parking lot now :",avaliable_lot)
         user_height_check = input("Enter 'y' if you car height >= 190\nEnter 'n' if you car height < 190\nEnter 'o' to select options : ")

         if user_height_check=='y':
            print("before :",avaliable_lot)
            print("-------------------------------")
            user_lot_input = input("Enter your parking lot :")

            user_lot_input in avaliable_lot
            over_location = avaliable_lot.index(user_lot_input)
            return_o_element = avaliable_lot.pop(over_location)
            oz[return_o_element[0]].append(return_o_element)
            oz[return_o_element[0]].sort()
                        
            print("ParkingBay :",user_lot_input[0])

            print("Over Parking lot empty now :",oz[return_o_element[0]])
            print("Amount :",len(oz[return_o_element[0]]))
            print("Avaliable lot after return lot :",avaliable_lot)
            break

         elif user_height_check=='n':
            print("Aaliable lot before return lot :",avaliable_lot)
            print("-------------------------------")
            n_user_lot_input = input("Enter your parking lot :")

            n_user_lot_input in avaliable_lot
            normal_location = avaliable_lot.index(n_user_lot_input)
            return_n_element = avaliable_lot.pop(normal_location)
            nz[return_n_element[0]].append(return_n_element)
            nz[return_n_element[0]].sort()
                        

            print("ParkingBay :",n_user_lot_input[0])
            print("Normal Parking lot empty now :",nz[return_n_element[0]])
            print("Amount :",len(nz[return_n_element[0]]))
            print("Avaliable lot after return lot :",avaliable_lot)
            break

         elif user_height_check=='o':
            return program()
                   
         else:
            print("----- Enter valid option bro !!! -----")
   
def program():
    try:
        while True:
         print("=============== Test2 ===============")
         print("1. Enter your car Height")
         print("2. Return Parking Bay")
         print("3. Close Program")
         ch=int(input("\tSelect option : "))
         if ch==1:
            get_lot()
         elif ch==2:
            return_lot()
            return program()
         elif ch==3:
            print("=============== Thank you ===============")
            break
         quit()   

    except:
        program()
program()