# Range
# x=range(10)
# print (list(x))
# y=range(0,10)
# print (list(y))
# z=range(0,10,2)
# print (list(z))

# # Concatinating string with num
# # x="Total states in USA: "
# # y=54
# # print(x+y)

# x="Total states in USA: "
# y="54"
# print(x+y)

# x="Total states in USA: "
# y=60
# print(x+str(y))

# # IF CONDITION
# # To get the max of two numbers
# a=int(input("Enter a number: "))
# b=int(input("Enter a number: "))
# if a>b:
#     print ("a is greater than b")
# elif a<b:
#     print ("a is lesser than b")
# else:
#     print ("a is equal to b")

# # To get the dish name from user and find its cuisine in list
# indian=["idly","vada","sambar"]
# chinese=["noodles","fried rice","bat soup"]
# italian=["pizza","pasta"]

# dish=str(input("Enter a dish: "))
# if dish in indian:
#     print ("indian")
# elif dish in chinese:
#     print("chinese")
# elif dish in italian:
#     print("italian")
# else:
#     print("Dont know")


# FOR LOOP
print("FL1")
nos=[1,2,3,4,5,66,77,88,100]
for x in nos:
    print(x)
    if x==5:
        break

print("FL2")
nos=[1,2,3,4,5,66,77,88,100]
for x in nos:
    if x==5:
        break
        print(x)

print("FL3")
nos=[1,2,3,4,5,66,77,88,100]
for x in nos:
    if x==5:
        break
    print(x)

print("FL4")
nos=[1,2,3,4,5,66,77,88,100]
for x in nos:
    if x==5:
        break
print(x)

print("FL1")
nos=[1,2,3,4,5,66,77,88,100]
for x in nos:
    print(x)
    if x==5:
        continue

print("FL2")
nos=[1,2,3,4,5,66,77,88,100]
for x in nos:
    if x==5:
        continue
        print(x)

print("FL3")
nos=[1,2,3,4,5,66,77,88,100]
for x in nos:
    if x==5:
        continue
    print(x)

print("FL4")
nos=[1,2,3,4,5,66,77,88,100]
for x in nos:
    if x==5:
        continue
print(x)

print("FL1")
nos=[1,2,3,4,5,66,77,88,100]
for x in nos:
    print(x)
    if x==5:
        pass

print("FL2")
nos=[1,2,3,4,5,66,77,88,100]
for x in nos:
    if x==5:
        pass
        print(x)

print("FL3")
nos=[1,2,3,4,5,66,77,88,100]
for x in nos:
    if x==5:
        pass
    print(x)

print("FL4")
nos=[1,2,3,4,5,66,77,88,100]
for x in nos:
    if x==5:
        pass
print(x)

# To get sum of list using for loop (Expenses)
Exp=[1400,1200,5000,6800,200]
total=0
for x in Exp:
    total=total+x
print(total)

for x in range(0,100):
    print (x)

for x in range(0,100,2):
    print (x)

# Finding key location
# This program is used to get the importance of break statement
# The code searches each element in the locations list and prints Key is not found in that element
# Once it identifies the location, it prints that key is found in that location
# After that it breaks the program. It is not continuing with the remaining items
# In practical life also, we will not search for key once it is found.
Key_location="table"
locations=["chair","shelf","table","bed"]
for x in locations:
    if x==Key_location:
        print("Key is found in ",x)
        break
    else:
        print("Key is not found in ",x)

# If you want to do the same operation number of times but except some elements or cases
# In this case, You have to use continue
# For example, To get square of all odd numbers between 1 to 10
# We can eliminate even numbers by using continue statement
for x in range(0,10):
    if (x%2==0):
        continue
    else:
        print(x*x)

# If you dont know the range and you want to stop the function based on a condition
# Use while loop in that case
# We have to do increment. If not, it will become never ending loop
x=0
while (x<=5):
    print(x)
    x=x+1

# Numeric Types
x=1
print(type(x))  

x=1
y=float(x)
print(type(x))
print(type(y))

x=1
y=complex(x)
print(type(y))
print(y)

a=10
b=3
print(a/b,a//b)

#Variable
a=5
a=8
print (a)

a=5
a="john"
print (a)
print (type(a))

a=5
A=8
print (a)
print (A)

# Strings
x="Balaji"
print (x[2])

x="Balaji"
for a in x:
    print (a)
    
x="Balaji"
print (len(x))

x="Balaji"
print ("a" in x)

x="My name is Balaji"
print ("is" in x)

x="My name is Balaji"
print ("was" in x)

x="Balaji"
print (x[2:4])

print("Modifying a string")
x="Balaji"
print(x.upper())

x="Balaji"
print(x.lower())

x="Balaji        "
print(x.strip())

x="      My name is Balaji        "
print(x.strip())

x="Balaji"
print(x.replace("B","K"))

# x="Balaji"
# x[0]=K
# print(x)

x="My name is Balaji"
print(x.split(" "))

x="My name is"
y="Balaji"
print(x+y)

x="My name is"
y="Balaji"
print(x+" "+y)

# x="Total states in USA: "
# y=54
# print(x+y)

x="Total states in USA: "
y="54"
print(x+y)

x="Total states in USA: "
y=54
print(x+str(y))

