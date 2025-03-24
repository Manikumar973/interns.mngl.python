#


#hear the two examples are keyword  variable length parameter
'''def a(**x):
    for k in x.items():
        print(k)
    else:
        print()


#main programme
a(rname="rossum")
a(sno=10,name="rs")
a(eno=20,ename="et",sal=4.5)
a(idn0=111,name="sandeep",hobby="reading")'''

'''
def a(**x):
    for k,v in x.items():
        print(k,v)
    else:
        print()
a(school="bag",sno=7893)
a(college="no books",rollno=123,travel="by bike")
a(king="queen",sno=98.3)
'''

#function deff
'''def totalmarks(**x):
    for i,d in x.items():
        print(i,d)
    else:
        print()
#function calls
totalmarks("rs","x",eng=84,tel=74,sci=73,soc=73)
totalmarks("js","sf",che=73,soc=83,math=84)'''

#keyword variable length parmeter

'''def totalmarks(**x):
    print(input("enter a name:"))
    print(input("enter a  sub:"))
    for i,y in x.items():
        print(i,y)
    else:
        print()
#function calls

totalmarks(tel=64,hin=73,math=93,sci=83,soc=84)
totalmarks(sci=74,soc=89,eng=83,phy=94)'''












#another example of keyword variable length parameter
#FUNCTION CALLS
'''def a(**x):
    for a in x.items():
        print(a)
#function calls
a(guntur='large area ',district="yes",pin=522529)
print("-"*50)
a(mangalagari="small area",district="no",pin=522003)
print("-"*50)
a(vijawada="large area",dictrict="yes",pn=522001)
print("-"*50)
a(ratnalacheruvu="small area",dictrict="no",pin=544562)
print("-"*50)
print("-------------THANKYOU------------------")
print("-"*50)
'''

#practice 3rd example of keyword varliable length parameters

'''def a(**x):
    for a,c in x.items():
        print(a,c)
    else:
        print()
a(bankname=": sbi",banklocation=": guntur",bankpin=123456)
a(college=": univ",location=": hyd",collegecode=": univ123")
a(school=": st anns",rollno="8778",classes=": 1 to 10th class")'''


#kpractice eyword variable length parameter
'''def a(**x):
    for i,y in x.items():
        print(i,y)


#main function
a(bus="large",wheels="4",gears=5)
a(car="small",size="small",gears=4)
a(bike="2 wheels",size="small",gears=4)'''


'''def a(**x):
    for i,j in x.items():
        print(i,j)
#main function
a(bike="2 wheeler",cost=12000,cc=200)'''



#variable length parameter example no 1
'''def mani(eno,ename,sal,dsg,cnt='india'):
    print("\t{}\t{}\t{}\t{}\t{}".format(eno,ename,sal,dsg,cnt))

#main programme
print("-"*50)
print("\tempno\tname\tsal\tdsg\tcountry")
print("-"*50)
mani(111,"ys",5.6,"tl")
mani(112,"dr","tl",4.5)
mani(113,"mr",8.7,412)
mani(114,"hf","junior","senior")
mani(115,"kr","senior","junior")
mani(116,sal=3000,dsg="king",ename="hr",cnt="usa")'''

#function deffination
'''def mani(eno,ename,esal,cnt="india"):
    print("\t{}\t{}\t{}\t{}".format(eno,ename,esal,cnt))

#main programme
print("-"*50)
print("\teno\tename\tesal\tindia")
print("-"*50)

mani(111,"kumar",3.6)
mani(112,"pavan",3.2)
mani(113,"kalyan",125)
mani(115,"kamal",12.5)
mani(116,"sandeep",esal=152255)'''









#function deffination
'''def a(eno,ename,esal,eloc,cnt="india"):
    print("\t{}\t{}\t{}\t{}\t{}".format(eno,ename,esal,eloc,cnt))

#main programme
print("-"*50)
print("\teno,\tename,\tesal,\teloc\t  india")
print("-"*50)
a(101,"mani",4.2,"guntur")
a(102,"kiran",4.2,"ppm")
a(103,"dinesh",4.8,"vij")
a(104,"mahi",4.9,"guntur")'''

#function deffination
'''def a(eno,ename,esal,eloc,cnt="india"):
    print("\t{}\t{}\t{}\t{}\t{}".format(eno,ename,esal,eloc,cnt))
#function call
print("\teno,\tename,\tesal,\teloc,\tcnt")
a(111,"mani",4.5,"gutur")
a(112,"kumar",4.8,"vijawada")'''


#variable length parameter
#function defination
'''def a(sno,sname,sclg,sloc,cnt="india"):
    print("\t{}\t{}\t{}\t{}\t{}".format(sno,sname,sclg,sloc,cnt))
#function calls
print("*"*50)
print("\tsno,\tsname\tsclg,\tloc\tindia")
print("*"*50)


a(111,"mani","univ","ppm")
a(112,"kamal","nri","nallapadu")
a(113,"simha","gec","gnt")'''


#variable length parameter
'''def a(sno,name,rollno,location,cnt="india"):
    print("\t{}\t{}\t{}\t{}\t{}".format(sno,name,rollno,location,cnt))
    #main function
print("-"*51)
print("\tsno,\tname,\trollno\tlocation\tindia")
print("-"*51)
a(111,"mani",123456,"hindupur")
a(112,"kalyan",321458,"guntur")
a(113,'kalyan',465665,"vijawada")
a(114,"kamal",659856,"kakinada")'''


#another example of variable length parameter

'''def findsum(name,*vals):
    s=0
    print("-"*40)
    print("hi,{}".format(name))
    for val in vals:
        print("{}".format(val),end=",")
        s=s+val
    else:
        print("sum",s)
        print()
#main programme
findsum("re",10,20)
findsum("kj",10,20,30)
findsum("jd",10,20,30,40)
findsum("hd",10,20,30,40,50)
'''

#example
#function definatuion
'''def totalmarks(**x):
    for sub,marks in x.items():
        print("\t{}\t{}".format(sub,marks))
    else:
        print()

#main programme
totalmarks=("fd","hdf",eng=84,tel=64,sci=73,math=74,soc=74)
totalmarks=("he","ur",phy=84,che=84)
totalmarks=("jd","hjd")
'''

#function deff
'''def totalmarks(**x):
    for i in x.items():
        print(i)
    else:
        print()


#function calls
totalmarks()'''



#local and global values
'''lang="python programming"
def ler1():
    crs1="ds"
    print("to print python program:",(crs1,lang))

def ler2():
    crs2="ml"
    print("to print python program:",(crs2,lang))

def ler3():
    crs3="java"
    print("to print python program:",(crs3,lang))'''

#function calls
#function defination
'''lang="global value"
city="hyd"
def mani1():
    crs1="hd"
    print("to implement",(crs1,lang))
    print(city)
def mani2():
    crs2="kg"
    print("to implement",(crs2,lang))
    print(city)
def mani3():
    crs3="ik"

    print("to implement",(crs3,lang))
    print(city)
#main programme
mani1()
mani2()
mani3()'''

'''
lang="python"
a=10

def updateval1():
    global lang,a
    lang=lang+"prog"
    a=a+1

print("val of lang before updateval1()=".format(lang))
print("val of 'a' after updateval1f()=".format(a))'''


#examples practicing global keyword
'''x = 10  # Global variable

def a():
    global x  # Declaring 'x' as global
    x = 20    # Modifying the global variable

a()
print(x) ''' # Output: 20


'''a=10
def updateval():
    global a
    a+a+1
    print("val of a in updateval()={}".format(a))

#main program
print(a)
updateval()
print(a)'''


#global key word variable practice
'''lang="python"
a=10

def updateval1():
    global lang,a
    lang=lang+"prog"
    a=a+1
def updateval2():
    global lang
    lang=lang+"lang"
    global a
    a=a*2'''

#main programme
'''print("val of lang before update1()={}".format(lang))
print("val of 'a' before update1()={}".format(a))
print("----------------")
updateval1()
print("--------------------------")
print("val of lang after update1()={}".format(lang))
print("val of 'a' before update1()={}".format(a))

updateval2()
print("val of lang after update2()={}".format(lang))
print("val of 'a' before update2()={}".format(a))'''















