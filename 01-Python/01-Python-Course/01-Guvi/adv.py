# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 09:46:09 2022

@author: Balaji Kannigesvaran
"""
#To find double of the inupt given using lambda function
# If we need tripler function, we can change f(2) to f(3)
def f(n):
    return lambda a:a*n

doub=f(2)
c=doub(33)
print(c)

# Filter function
def iseven (n):
    if (n%2==0):
        return True
    else:
        return False
num=[1,2,3,4,5,6,7,5]
evens=filter (iseven,num)
print(list(evens))

def iseven (n):
    return n%2==0
num=[1,2,3,4,5,6,7,5]
evens=filter (iseven,num)
print(list(evens))

num=[1,2,3,4,5,6,7,5]
evens=filter (lambda n:n%2==0,num)
print(list(evens))

# Similarly for filtering prime numbers
def prime(n):
    for x in range(2,n):
        if (n%x==0):
            return False
            break
    return True

numi=range(2,100)
num=list(numi)
primes=filter(prime,num)
print(list(primes))

num=[1,2,3,4,5,6,7,5]
squares=map(lambda n:n*n,num)
print(list(squares))

#Decorators
def div (a,b):
    print (a/b)
def newdiv(func):
    def inner (a,b):
        if (a<b):
            a,b=b,a
        return func(a,b)
    return inner
div = newdiv (div)
div (4,2)
div (2,4)


