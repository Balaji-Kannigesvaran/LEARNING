# -*- coding: utf-8 -*-
"""
Created on Wed Dec 22 18:27:44 2021

@author: Balaji Kannigesvaran
"""

#Defining 1D array
import numpy as np
a=np.array([20,30,40])
print (a)

#Defining 2D array
import numpy as np
a=np.array([[20,30,40],[50,60,70]])
print (a)

#Converting 1D list to array
import numpy as np
l=[20,30,40]
a=np.array(l)
print (a)

#Converting 2D list to array
import numpy as np
l=[[20,30,40],[50,60,70]]
a=np.array(l)
print (a)

#arange
import numpy as np
a1=np.arange(7)
print(a1)

a2=np.arange(7.0)
print(a2)

a3=np.arange(11,20)
print(a3)

a4=np.arange(11,20,2)
print(a4)

a5=np.arange(11,21,2)
print(a5)

#linspace
import numpy as np
a1=np.linspace(11,20)
print(a1)

import numpy as np
a1=np.linspace(11,20,7)
print(a1)

import numpy as np
a1=np.linspace(11,20,5)
print(a1)

import numpy as np
a1=np.linspace([1,5,11],20,5)
print(a1)

import numpy as np
a1=np.linspace([1,5,11],[10,15,20],5)
print(a1)

import numpy as np
a1=np.linspace(11,20,5,False)
print(a1)

import numpy as np
a1=np.linspace(11,20,5,False,True)
print(a1)

import numpy as np
a1=np.linspace(11,20,5,True,False,int)
print(a1)

import numpy as np
a1=np.linspace([1,5,11],20,5,True,False,int,0)
print(a1)

import numpy as np
a1=np.linspace([1,5,11],20,5,True,False,int,-1)
print(a1)

import numpy as np
a1=np.linspace(11,20,5,True,False,int,0)
print(a1)

import numpy as np
a1=np.linspace(11,20,5,True,False,int,-1)
print(a1)

#meshgrid
import numpy as np
x=np.array([1,2,3])
y=np.array([10,20,30])
z=np.meshgrid(x,y)
print(z)

import numpy as np
x=np.array([1,2,3])
y=np.array([10,20,30])
z=np.meshgrid(y,x)
print(z)

import numpy as np
xm,ym=np.mgrid[10:20:2,1:8:1]
print("xm:")
print(xm)
print(xm.shape)
print("ym:")
print(ym)
print(ym.shape)
print(xm,ym)

import numpy as np
xm,ym=np.mgrid[10:20:5j,1:8:8j]
print("xm:")
print(xm)
print(xm.shape)
print("ym:")
print(ym)
print(ym.shape)
print("xm,ym:")
print(xm,ym)

import numpy as np
xm,ym=np.ogrid[10:20:2,1:8:1]
print("xm:")
print(xm)
print(xm.shape)
print("ym:")
print(ym)
print(ym.shape)
print("xm,ym:")
print(xm,ym)
xg,yg=np.broadcast_arrays(xm,ym)
print("xg,yg:")
print(xg,yg)


import numpy as np
xm,ym=np.ogrid[10:20:5j,1:8:8j]
print("xm:")
print(xm)
print(xm.shape)
print("ym:")
print(ym)
print(ym.shape)
print("xm,ym:")
print(xm,ym)
xg,yg=np.broadcast_arrays(xm,ym)
print("xg,yg:")
print(xg,yg)

import numpy as np
a1=np.logspace(11,20,5)
print(a1)

import numpy as np
a1=np.geomspace(11,20,5)
print(a1)

#Creating array of zeros and ones
import numpy as np
a1=np.zeros(4)
print(a1)

import numpy as np
a1=np.zeros((2,3))
print(a1)

import numpy as np
a1=np.ones(4)
print(a1)

import numpy as np
a1=np.ones((2,3))
print(a1)

#To get size shape and datatype of an array
import numpy as np
a1=np.array([[1,2,3],[4,5,6]])
print(a1)
print(a1.size)
print(a1.shape)
print(a1.dtype)

#Create Random arrays
import numpy as np
a1=np.random.randint(10,50,5)
print(a1)

import numpy as np
a1=np.random.randint(10,50,(2,4))
print(a1)

#To get shape of the array
import numpy as np
a1=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(a1.shape)

#To access an element in the array
import numpy as np
a1=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(a1[2,1])
print(a1.item(2,1))

#Slicing
import numpy as np
a1=np.array([[1,2,3],[4,5,6],[7,8,9]])
a1[0,0]=11
a1.itemset((0,1),12)
print(a1)

import numpy as np
a1=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(a1)
print(np.take(a1,[0,3,6]))
np.put(a1,[0,3,6],[10,20,30])
print(a1)

import numpy as np
a1=np.array([1,2,3,4,5,6,7,8,9])
print(a1[5])
print(a1[:5])
print(a1[5:])
print(a1[:5:2])
print(a1[:8:3])

#For Multi Dimensional array
import numpy as np
a1=np.array([[1,2,3,4,5],[6,7,8,9,10],
             [11,12,13,14,15],[16,17,18,19,20],
             [21,22,23,24,25],[26,27,28,29,30]])
print(a1[0,2])
print(a1[2:])
print(a1[:2])
print(a1[2:5])
print(a1[2:5,2])
print(a1[2:5,2:4])
print(a1[:,2])
print(a1[::-1])
print(a1[::-2])
print(a1[::-3])
print(a1[::-4])
print(a1[::-8])

#Slicing using conditions
import numpy as np
a1=np.array([1,2,3,4,5,6,7,8,9])
even=a1[a1%2==0]
print(even)
a2=a1[a1>5]
print(a2)
a3=a1[(a1>5)&(a1<8)]
print(a3)
a4=a1[(a1>5)|(a1==2)]
print(a4)

import numpy as np
a1=np.array([2,2,2,4,6,6,10,10,9])
a2=np.unique(a1)
print(a2)

# reshaping arrays
import numpy as np
a1=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
a2=a1.reshape((3,4))
print(a2)
a3=a1.reshape((2,6))
print(a3)

import numpy as np
a1=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
a2=np.resize(a1,(3,4))
print(a2)
a3=np.resize(a1,(2,6))
print(a3)
a4=np.resize(a1,(2,5))
print(a4)
a5=np.resize(a1,(2,7))
print(a5)

#Transpose
import numpy as np
a1=np.array([[1,2,3],[4,5,6],[7,8,9]])
a2=a1.transpose()
print(a2)

import numpy as np
a1=np.array([[1,2,3],[4,5,6],[7,8,9]])
a2=a1.swapaxes(0,1)
print(a2)

# Flatten
import numpy as np
a1=np.array([[1,2,3],[4,5,6],[7,8,9]])
a2=a1.flatten()
print(a2)

import numpy as np
a1=np.array([[1,2,3],[4,5,6],[7,8,9]])
a2=a1.flatten('F')
print(a2)

# sort
import numpy as np
a1=np.array([[10,2,13],[64,8,46],[27,25,19]])
a2=np.sort(a1,0)
a3=np.sort(a1,1)
print(a1)
print(a2)
print(a3)

#Stacking
import numpy as np
a1=np.array([[1,2,3],[4,5,6],[7,8,9]])
a2=np.array([[11,12,13],[14,15,16],[17,18,19]])
a3=np.vstack((a1,a2))
a4=np.vstack((a2,a1))
a5=np.hstack((a1,a2))
a6=np.hstack((a2,a1))
print(a3,a4,a5,a6,sep='\n')

import numpy as np
a1=np.array([[1,2,3],[4,5,6],[7,8,9]])
a2=np.array([[11,12,13],[14,15,16],[17,18,19]])
a3=np.column_stack((a1,a2))
a4=np.column_stack((a2,a1))
a5=np.row_stack((a1,a2))
a6=np.row_stack((a2,a1))
print(a3,a4,a5,a6,sep='\n')

#Deleting arrays
import numpy as np
a1=np.array([[1,2,3],[4,5,6],[7,8,9]])
a2=np.delete(a1,1,0)
print(a2)
a3=np.delete(a1,1,1)
print(a3)

#Splitting
import numpy as np
a1=np.array([[1,2,3,4],[6,7,8,9],
             [11,12,13,14],[16,17,18,19],
             [21,22,23,24],[26,27,28,29]])
a2=np.hsplit(a1,4)
print(a2,sep="\n")
a3=np.hsplit(a1,(1,3))
print(a3,sep="\n")

#Copying arrays
import numpy as np
a1=np.array([[1,2,3],[4,5,6],[7,8,9]])
a2=a1
a1[0,0]=0
print(a1,a2,sep='\n')

import numpy as np
a1=np.array([[1,2,3],[4,5,6],[7,8,9]])
a2=a1.copy()
a1[0,0]=0
print(a1,a2,sep='\n')

#math
import numpy as np
a1=np.array([1,2,3,4,5])
a2=np.array([2,4,6,8,10])
print(a1+a2)
print(a1-a2)
print(a2-a1)
print(a1*a2)
print(a1/a2)
print(a2/a1)

import numpy as np
a1=np.array([[1,2,3,4,5],[11,12,13,14,15]])
a2=np.array([[2,4,6,8,10],[12,14,16,18,20]])
print(a1+a2)
print(a1-a2)
print(a2-a1)
print(a1*a2)
print(a1/a2)
print(a2/a1)

import numpy as np
a1=np.array([.1,.2,.3,.4,.5])
a2=np.array([2,4,6,8,10])
print(a1+a2)
print(a1-a2)
print(a2-a1)
print(a1*a2)
print(a1/a2)
print(a2/a1)

import numpy as np
a1=np.array([1,2,3,4,5])
a2=np.array([2,4,6,8,10])
print(np.add(a1,a2))
print(np.add(a1,1000))
print(np.subtract(a1,a2))
print(np.subtract(a2,a1))
print(np.subtract(a2,1))
print(np.multiply(a1,a2))
print(np.multiply(a1,4))
print(np.divide(a1,a2))
print(np.divide(a2,a1))
print(np.divide(a2,2))
print(np.remainder(a2,a1))
print(np.remainder(a2,3))
print(np.power(a2,a1))
print(np.power(a2,3))
print(np.sqrt(a2))
print(np.cbrt(a2))
a3=np.array([-2,-4,6,-8,10])
print(np.absolute(a3))
print(np.exp(a3))
print(np.log2(a2))
print(np.log10(a2))

#LCM and HCF(Greatest Common Divisor)
import numpy as np
a1=np.array([9,12,15])
print(np.gcd.reduce(a1))
print(np.lcm.reduce(a1))

# Floor and Ceiling
import numpy as np
a1=np.array([1.2,5.6,8.9])
print(np.floor(a1))
print(np.ceil(a1))

# Basic functions
import numpy as np
a1=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(a1.sum(axis = 0))
print(a1.sum(axis = 1))
print(a1.cumsum(axis = 0))
print(a1.cumsum(axis = 1))
print(a1.min(axis = 0))
print(a1.min(axis = 1))
print(a1.max(axis = 0))
print(a1.max(axis = 1))

#Finding max and min index and the value
import numpy as np
a1=np.array([[21,12,43],[64,25,76],[17,18,99],[49,62,38],[46,97,11]])
maxindex=a1.argmax(0)
print(maxindex)
maxnums=a1[maxindex]
print(maxnums)
maxindex=a1.argmax(1)
print(maxindex)
maxnums=a1[maxindex]
print(maxnums)
minindex=a1.argmin(0)
print(minindex)
minnums=a1[minindex]
print(minnums)
minindex=a1.argmin(1)
print(minindex)
minnums=a1[minindex]
print(minnums)

help(np.isnan)








