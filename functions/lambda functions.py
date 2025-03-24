'''def f1(a,b,c):pass


tempconvert=lambda c:1.8*c+32
print("type tempconert=",type(tempconvert))
tf=tempconvert(34)
print("temp in F.heat=",tf)'''




'''def mulop(a,b):
    c=a+b
    return c
mulop=lambda a,b:a*b

a=float(input("enter a  first name:"))
b=float(input("enter a  first name:"))
result=mulop(a,b)
print("mul({},{})={}".format(a,b,result))'''




#find big one

'''def findbig(a,b):
    if (a>b):
        return a
    else:
        return b
    findbig=lambda a,b:a if a>b else:b

#main programme
a=float(input("enter  a value:"))
b=float(input("enter  a value:"))
result=findbig(a,b)
print("big({},{})={}".format(a,b,result))'''


'''square = lambda x:x**2
print(square(5))


add= lambda x:x+25
a=int(input("enter  a value:"))
print(add(a))'''

'''mani=lambda x:x+15
print(mani(15))'''



#lambda function in one line
#which one is a big number

'''big=lambda a,b,c:"all values are equal"if(a==b)and (b==c) else a if(a>b) and (a>c) else b if(b>a) and (b>c) else c
print(big)

a=int(input("enter 1st  no"))
b=int(input("enter 2st  no"))
c=int(input("enter 3st  no"))
result=big(a,b,c)
print("big({},{},{})={}".format(a,b,c,result))'''
#print(a,b,c,result)

#mani=lambda a,b,c:  "all values are equal"if(a==b)and (b==c) else

'''big=lambda a,b,c:"all are equal" if (a==b) and (b==c) else a if a>b and a>c else b if b>a and b>c else c
print(big)
a=int(input("enter a value:"))
b=int(input("enter a value:"))
c=int(input("enter a value:"))
print("big({},{},{})={}".format(a,b,c,result))
print("result",big)'''

'''if a>=b and b>=a:
    print("a is big")
if b>=a and b>=c:
    print("b is big")
if c>=a and c>=b:
    print("c is big")'''


#1st approach
'''def a(b,c):
    d=b+c
    return d
res=a(15,45)
print(res)'''

#2nd approach
'''def a():
    a=int(input("enter a  no:"))
    b = int(input("enter a  no:"))
    c=a+b
    print(c)
a()'''























