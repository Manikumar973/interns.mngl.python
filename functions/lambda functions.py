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



#map function
'''print("enter old saries of employe:")
oldsal=[int(sal)for sal in input().split()]
newsal=tuple(map(lambda esal :esal*1.1,oldsal))
print("oldsalaries=",oldsal)
print("new salaries=",newsal)'''


#same example practice

'''print("enter old salaries of employee:")
oldsal=[int(sal)for sal in input().split()]
newsal=tuple(map(lambda esal: esal*1.1,oldsal))
print("old salaries=",oldsal)
print("new salaries=",newsal)'''


#original value and square value and sqrt value
'''print("enter  list of value:")
oldlist=[int(val)for val in input().split()]
squarelist=list(map(lambda n:n**2,oldlist))
sqrootlist=list(map(lambda k:k**0.5,oldlist))

print("original value:{}".format(oldlist))
print("square value:{}".format(squarelist))
print("squareroot value:{}".format(sqrootlist))'''


#maps sqrt
'''v=int(input("enter a  no:"))
def sqr(a):
    return a*a

#num=[1,2,3,4,5]
sqrs=list(map(sqr,v))
print(sqrs)
'''


'''def sqr(a):
    return a*a
num=[1,2,3,4,5]
sqrt=list(map(sqr,num))
print(sqrt)
'''


'''def a(s):
    return s*s
num=[1,2,3,4,5]
sqrt=list(map(lambda x:x*x,num))
print(sqrt)'''


#in this function maps and filter used

'''def sqr(a):
    return(a*a)
def fil(a):
    return a<=3
num=[1,2,33,4,5]
sqrt=list(filter(fil,num))
print(sqrt)'''




'''def a(s):
    return s*s
num=[1,2,57,3,6]
def fil(s):
    return s<4
sqrt=list(filter(fil,num))
print(sqrt)'''

#upper and lower

'''a=["mani","kumar"]
b=list(map(lambda x:x.upper(),a))
print(b)'''

'''k=["ndcnmkmsdn","jdhjjj"]
d=list(map(lambda x:x.upper(),k))
print(d)'''




'''n=[1,2,3,4,5]
s=list(map(lambda x:x**2,n))
print(s)'''

'''
a=[1,2,3,5,6,7,7,8,8,6,5,5,4,4]
b=list(map(lambda x:x**1.5,a))
print(b)

'''

'''
a=[1,2,3,3,4,5,6,8,8,5,84,5,6,7,8,555,7,5,444,6,885,335]
e=list(filter(lambda x:x%2==0,a))
print(e)'''




#redeuce function
'''
import functools
print("enter no of values seperated by spaces:")
nums=[int(val)for val in input().split()]
big=functools.reduce(lambda x,y:x if x>y else y,nums)
print("----------------------------------")
print("original elements={}".format(nums))
print("biggest element={}".format(big))
'''


























