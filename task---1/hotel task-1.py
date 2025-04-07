#import time
'''print("*"*100)
print("_________________________________________WELCOME_______________________________________")
print("*"*100)
#time.sleep(1.5)

print("-"*50)
print("menu displaying")
print("-"*50)


print("menu:    1.idly - 30")
print("         2.dosa - 40")
print("         3.poori - 40")
print("         4.bonda - 30")
print("         5.chapati - 40")
print("         6.sp.tea - 30")
print("         7.water bottel - 20")

item = int(input("enter a item no:(1/2/3/4/5/6/7):"))
quantity = int(input("enter a quantity:"))

#if item<=0:
 #   print("this is invalid input")

if item ==1:
    totalcost=quantity *30

elif item ==2:
    totalcost = quantity * 40
elif item ==3:
    totalcost = quantity * 40
elif item ==4:
    totalcost = quantity * 30
elif item ==5:
    totalcost = quantity * 40
elif item ==6:
    totalcost = quantity * 30
elif item ==7:
    totalcost = quantity * 20

else:
    print("invalid item selected.please try again.")
    totalcost=0

print("-"*100)
if totalcost>0:
    print(f"\n totalbill amount:{totalcost}")
    print("-" * 100)

else:
    print("bill calculation failed given input is rong")


print("_____________________________THANKYOU FOR VISITING__________________________")'''

# HOTEL BIRAYANIES POINT:

print("-"*50)
print("-------------WELCOME----------------------------")
print("-"*50)

print("menu:       1.birayani  - 120/-")
print("            2.chicken birayani  - 210/-")
print("            3.chicken dum birayani  - 250/-")
print("            4.mutton birayani  - 270/-")
print("            5.mutton dum birayani  - 300/-")
print("            6.chicken kabab  - 150/-")
print("            7.egg friderice  - 100/-")
print("            8.chicken  friderice - 120/-")
print(" " )
item =int(input("enter a item no:1/2/3/4/5/6/7/8:"))
print(" " )
if item<=0:
    print("this is invalid number")
quantity=int(input("enter a  quantity:"))

if item==1:
    totalcost = quantity*120
elif item==2:
    totalcost = quantity*210
elif item ==3:
    totalcost = quantity*250
elif item ==4:
    totalcost = quantity*270
elif item ==5:
    totalcost = quantity*300
elif item==6:
    totalcost = quantity*150
elif item ==7:
    totalcost = quantity*100
elif item ==8:
    totalcost = quantity * 120

else:
    print("invalid number please try again")
print(" ")
if totalcost>=0:
    print(f"totalbill amount:{totalcost}")
    print("\n")
cgst=totalcost*(1+13/100)

print("The cgst value is:",cgst)
cgstvalue=totalcost-cgst
print("The cgst value added to toatlbill:",cgstvalue)
#print("The cgst value is:",cgst)
#print("THE TOTAL BILL AMOUNT IS",cgst)
print("\n")
sgst=totalcost*(1+15/100)
print("The sgst value is :",sgst)
sgstvalue=totalcost-sgst
print("The sgst value added to toatlbill:",sgstvalue)
print("-"*100)
print("THE TOTAL BILL AMOUNT IS",sgst)
print("-"*100)
#print("\n")
print(" ")
print("--------thankyou___visit again--------")


#students marks list'''
'''rollno=int(input("please enter roll no:"))
if rollno>=0:
    print("it is a correct hallticket number")
else:
    print("rong hallticket number please try again")

name=input("enter name:")
s1=int(input("enter a sub-1 marks:"))
s2=int(input("enter a sub-2 marks:"))
s3=int(input("enter a sub-3 marks:"))
s4=int(input("enter a sub-4 marks:"))
s5=int(input("enter a sub-5 marks:"))
s6=int(input("enter a sub-6 marks:"))
total=s1+s2+s3+s4+s5+s6
print("student total marks:",total)
percentage=total/6
print("student average percentage:",percentage)

if s1<=35 or s2<=35 or s3<=35 or  s4<=35 or s5<=35 or s6<=35:

    #total=s1+s2+s3+s4+s5+s6
    #print(total)
    print("student are fail")
else:
    print("student are pass")
'''
















































































































