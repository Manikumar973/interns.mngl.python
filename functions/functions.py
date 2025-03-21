'''def a(c,d):
    e=c+d
    return(e)
res=a(10,20)
print(res)'''
from wsgiref.validate import validator

'''def a(mani,kumar):
    total=mani+kumar
    return(total)


result=a(300,200)
print(result)'''

'''def mani():
    a=float(input("enter a  no:"))
    b = float(input("enter a  no:"))
    c=a+b
    return(c)
kumar=mani()
print(kumar)'''



'''def a():
    c=int(input("enter a  no:"))
    d =int(input("enter a  no:"))
    e=c+d
    print (e)
res=a()
print(res)
'''

def disp(obj):
    #print(obj)

    for val in obj:
        print(val)



'''def show(obj):
    for k,v in obj.items():
        print(k,v)'''

'''print("list of values:")
lst=[10,20,45,35,-54,-45]
disp(lst)

print("set of values:")
set={23,45,67,43,23,56,23}
disp(set)

print("dict values")
d={10:"mani",20:"kumar",30:"king"}
disp(d)'''



'''def readvalues():
    lst=[]
    print("enter how many values you have:")
    n=int(input())
    for i in range(1,n+1):
        val=float(input("enter values:"))
        lst.append(val)
    return lst
def a(lst):
    s=0
    for val in lst:
        print(val)
        s=s+val
    else:
        print("sum:",(s))
        print("avg:",(s))
lst=readvalues()
a(lst)'''

#de fault para meters

'''def greet(name="guest"):
    print(f"hello,{name}!")
greet("captain")'''

'''def a(name="mani"):
    print(f"hello,{name}")
a("kumar")'''


'''def a(name="car"):
    print(f"tata,{name}")
a("indica")'''


'''def a(mani="king"):
    print(f"rebal,{mani}")
a("star")
'''
#variable length parameter of argument program
'''def info(eno,ename,emsal,emdg,cnt="india"):
    print("\t{}\t{}\t{}\t{}".format(eno,ename,emsal,emdg,cnt))
#main programme
print("\tempno\tempname\tsalary\temdg\tcountry")
info(111,"kumar",7.2,"senior","india")
info(112,"kumar",7.7,"tl","india")
info(113,7.8,"junior","kalyan","india")
info(114,"pavan",7522,"jr mutyam")
#info(112,"king",6,2,"junior")
info(115,"sc",emsal=8.8,emdg="king kumar")'''




#varriable length perameter
'''def a(eno,ename,esal,edg,cnt):
    print("\t{}\t{}\t{}\t{}".format(eno,ename,esal,edg,cnt))

#main programme
print("\teno\tname,\tesal,\tedg,\tcountry")
a(111,"rs",5.6,"senior","india",)
a(112,"mani",855,"junior","pakistan")
a(113,"kaleja",5.7,"jr","dubai")
a(eno=114,ename="dhoni",esal=7500,edg="ceo",cnt="arab")'''

'''def dispempinfo(eno,ename,sal,cnt="india"):
    print("\t{}\t{}\t{}\t{}".format(eno,ename,sal,cnt))
#main programme
print("\tempno\tename\tsal\tcnt")'''


'''def add_numbers(*args):
    total = sum(args)
    print(f"Total: {total}")

add_numbers(10, 20, 30)    # Output: Total: 60
add_numbers(5, 15)  '''       # Output: Total: 20


'''def add_numbers(*numbers):
    total = sum(numbers)
    print("Total:", total)

add_numbers(10, 20)           # Output: Total: 30
add_numbers(5, 15, 25, 35)'''# Output: Total: 80




'''def sum(a,b):
    c=a+b
    return c
sum(10,20)
print("sum={}".format(sum))
'''

#method 1

'''def a(a,b,c):
    d=a+b+c
    return d
res=a(20,30,40)
print(res)'''


#method 2
'''def a():
    a=int(input("enter a no:"))
    b = int(input("enter a no:"))
    c = int(input("enter a no:"))
    d = int(input("enter a no:"))
    e=a+b+c+d
    print(e)

a()
'''
#method 1 and 2

'''def a(a,b,c):
    d=a+b+c
    return(d)
res=a(10,20,30)
print(res)'''

'''def a():
    a=int(input("enter a  value:"))
    b = int(input("enter a  value:"))
    c = int(input("enter a  value:"))
    d=a+b+c
    print(d)
a()'''

#method 3

'''def a():
    a=float(input("enter a value:"))
    b = float(input("enter a value:"))
    c = float(input("enter a value:"))
    d=a+b+c
    print(d)
a()'''


#variable length parameter of arguments programs
'''
def mani(eno,ename,sal,dsg,cnt='india'):
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
mani(116,sal=3000,dsg="king",ename="hr",cnt="usa")

print("-"*50)'''










