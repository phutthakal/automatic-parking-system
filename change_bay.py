bay_order=["A","F","C","B","G","D","H","E"]
parked_lot=[]
zone_order=["1","2"]
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

z={"A":zone_order[0],"B":zone_order[0],"C":zone_order[1],"D":zone_order[1],"E":zone_order[1],"F":zone_order[1],"G":zone_order[1],"H":zone_order[1]}


try:
    print(bay_order)
    list_input = input("Parking Bay: ")
    if list_input  in bay_order:
         bay_order.remove(list_input)
         bay_order.append(list_input)
         print(nz[list_input])
                
         list_lot = input("Parking Lot: ")
         if list_lot not in parked_lot:
            parked_lot.append(list_lot)
            nz[list_input].remove(list_lot)
            print("Bay: ", list_input)
            print("Lot: ", parked_lot)

    if list_input in bay_order:
        bay_order.remove(list_input)
        bay_order.append(list_input)
        print("********************************************")
        print("Parking Bay: ", bay_order[7])
        print("Parking Lot: ", parked_lot)
        list_a = input("Want to change Bay y/n: ")
        print("***********************************************")
        
        if list_a == "y":
            parked_lot.clear()
            print(bay_order)
            in_bay = input("Bay: ")
            
            if in_bay  in bay_order:
                bay_order.remove(in_bay)
                bay_order.append(in_bay)
                print(nz[in_bay])
                
                in_lot = input("Lot: ")
                if in_lot not in parked_lot:
                  parked_lot.append(in_lot)
                  nz[in_bay].remove(in_lot)
                  print("***********************************************")
                  print("Next Bay:", in_bay)
                  print("Next Lot:", parked_lot)
            else:
                print("Invalid bay selected.")
        else:
            print("Thank you.")
    else:
        print("Invalid bay selected.")
except:
    print("Error.")