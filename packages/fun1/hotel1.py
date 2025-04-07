
student="student1"
teacher="teacher1"


rollno=int(input("please enter roll no:"))
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