#looping statements
#for loop

'''a=[1,2,3,4,5,6,7,8,9]
print(a)
for i in a:
    print(i,end=",")'''




'''b=[10,20,30,40]
for a in b:
    print(a)'''

#for i in range(1,100):
#    print(i,end=",")


#to print (even numbers)

'''for i in range(0,102,2):
    print(i,end=",")'''

#To print(odd numbers)
'''for i in range(1,100,2):
    print(i,end=",")'''

#print multiplication tables
'''num=5
for i in range(1,11):
    print(f"{num}*{i}={num*i}")'''

'''fruits = ["Apple", "Banana", "Cherry", "Mango"]
for index, fruit in enumerate(fruits, start=1):
    print(f"{index}. {fruit}")
    print(type(fruits))'''

#using while to run the programme

'''while True:
    print("hii iam mani")
    break'''

'''n=int(input("enter a  no:"))
if n<=0:
    #print("{}is invalid input".format(n))
    print()
else:
    i=1
    while(i<=n):
        print(i,end=",")
        i=i+1
'''


'''n=int(input("enter a  no:"))
if n<=0:
    print()
else:
    i=1
    while(i<=n):
        print(i,end=",")
        i+=1'''

#forloop and whileloop
'''count=0
while count<=5:
    print(count)
    count+=1'''

'''for i in range(0,21):
    print(i,end=",")'''

'''count=0
while count<21:
    print(count,end=",")
    count+=1'''


'''fruits=["apple","banana","goa","graphes"]
for i in fruits:
    print([i]*3)'''


'''a=input("enter any thing:")
for i in a:
    print(i,end=",")'''

'''k=18
while k<20:
    print("hi")
    k+=1'''


'''mani=1
while mani<10:
    print("hi ra mani")
    break
'''

'''for i in range(1,5):
   for j in range(1,5):
    #    for k in range(4,5):
            print(i,j,end=",")'''


'''for i in range(0,5):
    for j in range(1,4):
        print(i,j,end=",")'''




'''answer = ""
while answer != "yes":
    answer = input("Type 'yes' to stop: ")
print("You typed 'yes'. Loop stopped.")
'''

'''answer=" "
while answer !="yes":
    answer = input("type 'yes to stop: ")
print("iam types yes loop stop")'''




'''a="hii mani"
for i in a:
    if i=="ma":
        break
    print(i,end=",")'''



'''a="manikumar"
for i in a:
    if i=='k':
        break
    print(i)'''


#while loop practicing
'''n=int(input(("enter a  no:")))
if(n<=0):
    print()
else:
    i=1
    while(i<=n):
        print(i,end=",")
        i+=1'''


'''n=int(input("enter a  no:"))
if n<=0:
    print()
else:
    i=1
    while i<=n:
        print(i)
        i+=1'''






'''a=int(input("enter a  no:"))
if a<=0:
    print()
else:
    i=1
    while i<=a:
        print(i)
        i+=1
'''


'''a=int(input("enter a  no:"))
if a<=0:
    print()
else:
    i=a
    while i>=1:
        print(i)
        i-=1'''


'''a=int(input("enter a no:"))
if a<=0:
    print()
else:
    i=a
    while i>=1:
        print(i)
        i-=1
'''
'''
n=int(input("enter a  value:"))
if n<=0:
    print()
else:
    i=n
    while i>=1:
        print(i)
        i-=1'''




'''

n=int(input("enter a  value:"))
if n<=0:
    print()
else:
    i=1
    while i<=n:
        print(i)
        i+=1
'''


'''n=int(input("enter a value:"))
i=1
while i<=n:
    print(" ")'''


#while
'''a=int(input("enter a value:"))
i=1
while (i<=a/2):
    if a%i==0:
        print(i)
    i+=1'''



'''a=input("enter a  no:")
for i in a:
    print(i,end=",")'''

#any number giving a sum
'''s=0
n=input("enter a value:")
for i in n:
    x=int(i)
    s=s+x
else:
    print("sum({})={}".format(n,s))'''


'''s=0
n=input("enter a value:")
for i in n:
    x=int(i)
    s=s+x
else:
    print(f"The answer is: {n,s}")
    print("The answer is:", n,s)'''



# for 1 to any no
'''n=int(input("enter a  no:"))
if n<=0:
    print()
else:
    i=1
    while i<=n:
        print(i)
        i+=1'''

#for back to one
'''n=int(input("enter a  value:"))
if n<=0:
    print()
else:
    i=n
    while i>=1:
        print(i)
        i-=1'''


#how to add numbers
'''s=0
n=input("enter vale:")
for i in n:
    x=int(i)
    s=s+x
else:
    print(f"the answer is:{n,s}")'''

# practice problem
'''n=int(input("enter a no:"))
if(n<=0):
    print()
else:
    l=list()
    for i in range(1,n+1):
        val=float(input("enter {} value:".format(i)))
        l.append(val)
    else:
        s=0
        print("content of list={}".format(l))
        for val in l:
            s=s+val
        else:
            print("sum={}".format(s))
            print("avg={}".format(s/n))'''



#nested or inner loops in python

'''for i in range(1,5):
    print(f"the answer is:{i}")
    print("-"*100)
    for j in range(1,5):
        print(f"the answer is:{j}")
        print("-"*100)'''

#loops

'''for i in range(5,0,-1):
    print("outer loop=",i)
    print("-"*100)
    j=3
    while(j>0):
        print("val of j=",j)
        j=j-1
    else:
        print("outer of inner loop")
        print("-"*100)

else:
    print("out of outer for loop")'''



#to print  a no in a list

'''lst=[3,14,19,9,7,-45,0,8]
for n in lst:
    if(n<=0):
        print("{} is invalid input".format(n))
        #print(f"the answer is:{n}")
    else:
        print("*"*100)
        print("mul table of {}".format(n))
        print("*"*100)
        for i in range(1,11):
            print("\t{}*{}={}".format(n,i,n*i))

        else:
            print("*"*100)'''


'''a=[2,3,4,5,25,-9,37,-6]

for n in a:
    if (n<=0):
        pass
        #print("don't print negative value",n)
    else:
        print("----------------------")
        print("mul table of {}".format(n))
        print("------------------------------")
        for i in range(1,11):
            print("\t{}*{}={}".format(n,i,n*i))
        else:
            print("-----------------------")'''




