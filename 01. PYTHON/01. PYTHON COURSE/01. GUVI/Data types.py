"""
Created on Fri Dec 10 15:19:38 2021
@author: Balaji Kannigesvaran
"""
""" l is list, a is array, t is tuple, s is set, d is dictionary """
# import numpy as np
# import array

# l=["car","bike",30,40,3.0,True]
# a=np.array([10,20,30.92],dtype="float")
# # a=array.array('i',["car","bike","scooter"])
# t=("car","bike",30,40,3.0,True)
# s={"car","bike",30,40,3.0,True}
# f=frozenset(["car","bike",30,40,3.0,True])
# l2=list(("car","bike",30,40,3.0,True))
# print(l,t,s,a,f)

# print(l[0],t[0],s,f,l2)


#Defining data types

l = list(("car","bike",30,40,3.0,True))
print(l)
l = ["car","bike",30,40,3.0,True]
print(l)
import array
a=array.array('i',[20,30,40])
print(a)

# Giving float in int typecode will give type error
# import array
# a=array.array('i',[20,30,40,5.0])
# print(a)

import numpy as np
a=np.array([20,30,40])
print(a)
a=np.array((20,30,40.92))
print(a)
a=np.array((20,30,40.92), dtype="int")
print(a)
a=np.array([20,30,40.92], dtype="float")
print(a)
t = ("car","bike",30,40,3.0,True)
print(t)
s = {"car","bike",30,40,3.0,True}
print(s)

t = tuple(("car","bike",30,40,3.0,True))
print(t)
t = tuple(["car","bike",30,40,3.0,True])
print(t)
t = ("car","bike",30,40,3.0,True)
print(t)

s = set(("car","bike",30,40,3.0,True))
print(s)
s = set(["car","bike",30,40,3.0,True])
print(s)
s = {"car","bike",30,40,3.0,True}
print(s)

f = frozenset(("car","bike",30,40,3.0,True))
print(f)
f = frozenset(["car","bike",30,40,3.0,True])
print(f)

d=dict({"Name":"Balaji","Age":26})
print(d)
d={"Name":"Balaji","Age":26}
print(d)

# Property
# 1)Ordered
# Lists are ordered
l = ["car","bike",30,40,3.0,True]
print(l[0],l[2],l[5])

# arrays are ordered
import numpy as np
a=np.array([20,30,40,50,60,70])
print(a[0],a[3],a[5])

# tuples are ordered
t = ("car","bike",30,40,3.0,True)
print(t[0],t[2],t[5])

# # sets are not ordered
# s = {"car","bike",30,40,3.0,True}
# print(s[0],s[2],s[5])
s1 = {"car","bike",30,40,3.0,True}
s2 = {30,40,True,"car","bike",3.0,True}
if (s1==s2):
    print("s1 and s2 are same")
else:
    print("s1 and s2 are not same")


# # Frozen sets are not ordered
# f = frozenset(["car","bike",30,40,3.0,True])
# print(f[0],f[2],f[5])
f1 = frozenset(("car","bike",30,40,3.0,True))
f2 = frozenset((30,40,True,"car","bike",3.0,True))
if (f1==f2):
    print("f1 and f2 are same")
else:
    print("f1 and f2 are not same")


# # Dictionaries are not ordered
# d={"Name":"Balaji","Age":26}
# print(d[0])

# But we can call the item in the dictionary by using keys
d1={"Name":"Balaji","Age":26}
d2={"Age":26,"Name":"Balaji"}
if (d1==d2):
    print("d1 and d2 are same")
else:
    print("d1 and d2 are not same")

d={"Name":"Balaji","Age":26}
print(d["Name"])

print("To access items in the list:",sep="\n")
l = ["car","bike",30,40,3.0,True]
print(l[0],l[2],l[5])

l = ["car","bike",30,40,3.0,True]
print(l[2:5])

l = ["car","bike",30,40,3.0,True]
print(l[2:])

l = ["car","bike",30,40,3.0,True]
print(l[:5])

print("To access items in the array:",sep="\n")
import numpy as np
a=np.array([20,30,40,50,60,70])
print(a[0],a[2],a[5])

import numpy as np
a=np.array([20,30,40,50,60,70])
print(a[2:5])

import numpy as np
a=np.array([20,30,40,50,60,70])
print(a[2:])

import numpy as np
a=np.array([20,30,40,50,60,70])
print(a[:5])

print("To access items in the tuple:",sep="\n")
l = ["car","bike",30,40,3.0,True]
print(t[0],t[2],t[5])

l = ["car","bike",30,40,3.0,True]
print(t[2:5])

l = ["car","bike",30,40,3.0,True]
print(t[2:])

l = ["car","bike",30,40,3.0,True]
print(t[:5])

print("To access items in the set:",sep="\n")
s = {"car","bike",30,40,3.0,True}
30 in s

for i in s:
    print(i)

print("To access items in the frozenset:",sep="\n")
f = frozenset(["car","bike",30,40,3.0,True])
30 in f
f = frozenset(["car","bike",30,40,3.0,True])

for i in f:
    print(i)

print("To access items in the dictionary:",sep="\n")
d={"Name":"Balaji","Age":26}
x=d["Name"]
print (x)

d={"Name":"Balaji","Age":26}
x=d.get("Name")
print (x)

# 2)Changable/ Mutable
# Lists are Changable/Mutable
l= ["car","bike",30,40,3.0,True]
l[1]="Scooters"
print(l)

l = ["car","bike",30,40,3.0,True]
l.insert(3,"Scooters")
print(l)

l = ["car","bike",30,40,3.0,True]
l.append("Scooters")
print(l)

l = ["car","bike"]
l.extend([30,40,3.0,True])
print(l)

l = ["car","bike",30,40,3.0,True]
l.remove("bike")
print(l)

l = ["car","bike",30,40,"bike",3.0,True]
l.remove("bike")
print(l)

l = ["car","bike",30,40,3.0,True]
l.pop(2)
print(l)

l = ["car","bike",30,40,3.0,True]
l.pop()
print(l)

l = ["car","bike",30,40,3.0,True]
del l[2:]
print(l)

# arrays are Changable/Mutable
import numpy as np
a=np.array([20,30,40,50,60,70])
a[1]=5000
print(a)

a=np.array([20,30,40,50,60,70])
a1 = np.insert(a, [2], 80)
print(a1)

a=np.array([20,30,40,50,60,70])
a1=np.append(a,80)
print(a1)

a=np.array([20,30,40,50,60,70])
a1=np.append(a,(80,90))
print(a1)


# tuples are Unchangable/Immutable
# t = ("car","bike",30,40,3.0,True)
# t[1]="Scooters"
# print(t)

t = ("car","bike",30,40,3.0,True)
l1=list(t)
l1[1]="Scooters"
t=tuple(l1)
print(t)

# #Sets are unchangable
# s = {"car","bike",30,40,3.0,True}
# s[1]="Scooters"
# print(s)

s = {"car","bike",30,40,3.0,True}
l1=list(s)
l1[1]="Scooters"
s=set(l1)
print(s)

s = {"car","bike",30,40,3.0,True}
s.add(5)
print(s)

s = {"car","bike",30,40,3.0,True}
s.remove(30)
print(s)

# #Frozen Sets are unchangable
# f = frozenset(["car","bike",30,40,3.0,True])
# f[1]="Scooters"
# print(f)

f = frozenset(["car","bike",30,40,3.0,True])
l1=list(f)
l1[1]="Scooters"
f=frozenset(l1)
print(f)

# dictionaries are Unchangable/Immutable
d={"Name":"Balaji","Age":26}
d["Name"]="Krishna"
print (d)

d={"Name":"Balaji","Age":26}
d.update({"Name":"Krishna"})
print (d)

d={"Name":"Balaji","Age":26}
d["City"]="Chennai"
print (d)

# 3)Allows duplicates
# lists allows duplicates
l = ["car","bike",30,40,3.0,True,"car"]
print(l)

# arrays allows duplicates
a=np.array([20,30,40,40])
print(a)

# tuples allows duplicates
t = ("car","bike",30,40,3.0,True,"car")
print(t)

# Sets doesn't allows duplicates
s = {"car","bike",30,40,3.0,True,"car"}
print(s)

# FrozenSets doesn't allows duplicates
f = frozenset(["car","bike",30,40,3.0,True,"car"])
print(f)

# # Dictionaries doesn't allows duplicates
# d={"Name":"Balaji","Age":26,"Name":"Krishna"}
# print (d)

# To get the length
l= ["car","bike",30,40,3.0,True]
print(len(l))

a=np.array([20,30,40,50,60,70])
print(len(a))

t = ("car","bike",30,40,3.0,True)
print(len(t))

s = {"car","bike",30,40,3.0,True}
print(len(s))

f = frozenset(["car","bike",30,40,3.0,True])
print(len(f))

d={"Name":"Balaji","Age":26}
print(len(d))

# To get data type of list
l= ["car","bike",30,40,3.0,True]
print(type(l))

a=np.array([20,30,40,50,60,70])
print(type(a))

t = ("car","bike",30,40,3.0,True)
print(type(t))

s = {"car","bike",30,40,3.0,True}
print(type(s))

f = frozenset(["car","bike",30,40,3.0,True])
print(type(f))

d={"Name":"Balaji","Age":26}
print(type(d))


# Arrays Additional functions
a=np.array([20,30,40,50,60,70,80,90,100])
a_2d=a.reshape(3,3)
print(a_2d)

a=np.array([20,30,40,50,60,70,80,90,100])
a_2d=a.reshape(3,3)
a1=np.append(a_2d,[[110,120,130]],axis=0)
print(a1)

# a=np.array([20,30,40,50,60,70,80,90,100])
# a_2d=a.reshape(3,3)
# a1=np.append(a_2d,[[110,120,130]],axis=1)
# print(a1)

a=np.array([20,30,40,50,60,70,80,90,100])
a_2d=a.reshape(3,3)
a1=np.append(a_2d,[[110],[120],[130]],axis=1)
print(a1)

# sets Additional functions
l=[1,1,2,2,2,3,3,3,3,3,4]
s=set(l)
print(s)

s1={1,1,2,3,4}
s2={1,5}
Union=s1|s2
print(Union)

s1={1,1,2,3,4}
s2={1,5}
Intersection=s1&s2
print(Intersection)

s1={1,1,2,3,4}
s2={1,5}
Difference=s1-s2
print(Difference)

s1={1,1,2,3,4}
s2={1,5}
Difference=s2-s1
print(Difference)

s1={1,1,2,3,4}
s2={1,5}
Symmetric_Difference=s1^s2
print(Symmetric_Difference)

#To concatenate 2 lists
l1 = ["car","bike",30]
l2 = [40,3.0,True]
l=l1+l2
print(l)

# l1 = ["car","bike",30]
# l=l1+"Bike"
# print(l)

# To concatenate 2 arrays
import numpy as np
a1=np.array([20,30,40])
a2=np.array([50,60,70])
a=a1+a2
print(a)

# To concatenate 2 tuples
t1 = ("car","bike",30)
t2 = (40,3.0,True)
t=t1+t2
print(t)

t1 = ("car","bike",30)
t=t1+"bike"
print(t)

# To concatenate 2 Sets
s1 = {"car","bike",30}
s2 = {40,3.0,True}
s=s1+s2
print(s)

# To concatenate 2 frozen sets
f1 = frozenset(["car","bike",30])
f2 = frozenset([40,3.0,True])
f=f1+f2
print(f)

# To concatenate 2 dictionaries
d1={"Name":"Balaji","Age":26}
d2={"Name":"Shiva","Age":26}
d=d1+d2
print(d)






