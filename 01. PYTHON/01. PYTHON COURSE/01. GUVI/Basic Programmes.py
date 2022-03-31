#String Reverse & Palindrome
def palindrome1(ipstr):
  revstr = list(ipstr)
  left = 0
  right = len(revstr)-1
  while left<right:
    tempVar= revstr[left]
    revstr[left]= revstr[right]
    revstr[right]= tempVar
    left += 1
    right -= 1
  print(revstr)
  if (list(ipstr)==revstr):
    print( "This is a Palindrome")
  else:
    print("This is not a Palindrome")
palindrome1("MALAYALAM")


#Palindrome Only
def palindrome2(ipstr):
  str = list(ipstr)
  left = 0
  right = len(str)-1
  while left<right:
    if (str[left]==str[right]):
      left += 1
      right -= 1
      State = True
    else:
      State = False
      break
  if (State):
    print( "This is a Palindrome")
  else:
    print("This is not a Palindrome")
palindrome2("High")


#Palindrome Using Negative Indexing
def palindrome3(ipstr):
  str = list(ipstr)
  for i in range (0,(len(str))//2):
    if str[i] == str [-(i+1)]:
      State = True
    else:
      State = False
      break
  if (State):
    print( "This is a Palindrome")
  else:
    print("This is not a Palindrome")
palindrome3("MALAYALAM")


def primeNum(num):
  if num ==2:
    State = True
  for x in range (2,num):
    if num%x==0:
      State = False
      break
  else:
    State = True
  
  if State:
    print ("Prime")
  else:
    print ("Not Prime")

primeNum(2)


# fibbonacci Series
def fib(num):
  if num<1:
    print ("invalid input")
  else:
    a,b=0,1
    if (num==1):
      print (a)
    else:
      print (a,b,sep='\n')
    for x in range (2,num):
      c=a+b
      a,b=b,c
      print (c)

fib(4)

n = 5
def fibonacci(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibonacci(num-1)+fibonacci(num-2)
print("fibonacci series are : ")
for i in range(0,n):
    print(fibonacci(i))

# factorial
def fact(num):
  f=1
  for x in range(1,num+1):
    f=f*x
  print (f)
fact(6)

def fact(num):
  if num==0:
    return 1
  else:
    return (num) * (fact(num-1))

Factorial = fact(8)
print (Factorial)


# linear Search
def search(num, list):
  for x in range (0,len(list)):
    if(num==list[x]):
      state=True
      break
  else:
    state=False

  if (state):
    print ("Found")
  else:
    print ("Not Found")

list1 = [1,2,4,5,6,8,9,3]
num1=9
num2=3
num3=10
search (num1,list1)
search (num2,list1)
search (num3,list1)


# binary Search
#Works only when it is sorted
def binsearch(num, list):
  l=0
  u=len(list)
  while l<=u:
    mid=(l+u)//2
    if(num==list[mid]):
      return True
    else:
      if(list[mid]<num):
        l=mid+1
      else:
        u=mid-1

  return False

lst1 = [1,2,4,5,6,8,90]
numb1=30
state = binsearch (numb1,lst1)
if (state):
  print ("Found")
else:
  print ("Not Found")


# Bubble sort
def sort(nums):
  for i in range(len(nums)-1,0,-1):
    for j in range (i):
      if nums[j]>nums[j+1]:
        temp = nums[j]
        nums[j]=nums[j+1]
        nums[j+1]=temp
nums = [5,3,8,6,7,2]
sort(nums)
print(nums)

#Selection Sort
def selsort(nums):
  for i in range(len(nums)):
    minpos=i
    for j in range (i,len(nums)):
      if nums[j]<nums[minpos]:
        minpos=j
      temp = nums[i]
      nums[i]=nums[minpos]
      nums[minpos]=temp

nums = [5,3,8,6,7,2]
selsort(nums)
print(nums)

numip=153
n=numip
armstrongNum=0
while n!=0:
  armstrongNum += (n%10)**3
  n=n//10
if (numip==armstrongNum):
  print ("Armstrong num")
else:
  print ("Not Armstrong num")