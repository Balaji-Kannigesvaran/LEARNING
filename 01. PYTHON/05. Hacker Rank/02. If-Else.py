# -*- coding: utf-8 -*-
"""
Created on Mon Jan 10 11:17:43 2022

@author: Balaji Kannigesvaran
"""
import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())
    if (n%2!=0):
        print ("Weird")
    else:
        if ((n>=2) & (n<=5)):               #Use bracket seperately. Or it wont work properly
            print ("Not Weird")
        elif ((n>=6) & (n<=20)):            #Use bracket seperately. Or it wont work properly
            print ("Weird")
        else:
            print ("Not Weird")

# Combining statements
if __name__ == '__main__':
    n = int(input().strip())
    if (n%2==0 & (((n>=2) & (n<=5)) | (n>20))):  #Use bracket seperately. Or it wont work properly
        print ("Not Weird")
    else:
        print ("Weird")
        
# Using Dictionary
n = int(input().strip())
check = {True: "Not Weird", False: "Weird"}

print(check[
        n%2==0 and (
            n in range(2,6) or 
            n > 20)
    ])


n = int(input().strip())
if n%2==0 and (n in range(2,6) or n>20 ):
    print ("Not")
print ("Weird")
        