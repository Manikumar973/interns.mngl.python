'''mani="birayani"

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
'''


#bir1.py example
def wish(val):
    print("{} good evening".format(val))



























