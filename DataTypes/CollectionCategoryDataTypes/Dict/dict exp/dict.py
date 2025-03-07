'''d1={"apple":23.54,"kiwi":34,"sberry":100}
print(d1)
print(type(d1))
print(id(d1))
mani=(d1)
print(mani)
for x in d1:
  print(x)
'''

#keys and values
'''d1={"apple":23.54,"kiwi":34,"sberry":100}
print(d1.keys())
for a in d1:
    print(a)'''

#shallow copy
'''d1={"apple":23.54,"kiwi":34,"sberry":100}
print(d1,id(d1))
d2=d1.copy()
print(d2)
print(d2,id(d2))
d2["sberry"]=100
d1["guava"]=60
d1["mango"]=787
print(d1)'''

'''d1={"praveen":"python","kiran":"java"}
d2={"rs":"django","dr":"c"}
d3=d1.update(d2)
print(d1)
print(d2)
print(d3)
d1={"praveen":"python","kiran":"java"}
d2={"praveen":"django","dr":"c"}

d1.update(d2)
print(d1)
print(d2)

d2.update(d1)
print(d2)'''

'''d1=dict()
d1["apple"]=6899
d1["ball"]=77889
d1["cat"]=888776
print(d1)

d1={"praveen":"python","kiran":"java"}
'''

d1=dict()
d1["mani"]=799
d1["ball"]=525
d1["cat"]=565656
print(d1)


d1={"praveen":"python","kiran":"java","apple":23.54,"kiwi":34,"sberry":100}
d1.pop("kiran")
print(d1)

d1.popitem()
print(d1)

















































