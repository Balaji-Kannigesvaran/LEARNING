# -*- coding: utf-8 -*-
"""
Created on Mon Jan 10 12:55:46 2022

@author: Balaji Kannigesvaran
"""

if __name__ == '__main__':
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    sum = a+b
    sub = a-b
    prod = a*b
    
    print (sum,sub,prod,sep='\n')
    print (a+b,a-b,a*b,sep='\n')
    print ("Based on string formatting")
    print('{:d}\n{:d}\n{:d}'.format(a+b,a-b,a*b))
    print(f"{a+b}\n{a-b}\n{a*b}")   #Here, f represents fstrings
    