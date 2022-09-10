# STAAD MODEL GENERATOR
import math as ma
import numpy as np
import pandas as pd

L = 200
B = 100
EC_Ht = 12
Slope = 20
RC_Ht = (B/Slope)+EC_Ht
CS_L=10                                                                         #Column Spacing along Length
CS_B=10                                                                         #Column Spacing along Width
NC_L=(L/CS_L)+1                                                                 #No of columns along Length
NC_B=(B/CS_B)+1                                                                 #No of columns along Width
print ('Joint Coordinates')
JC=np.empty()
ORIGIN=1
for i in range (0,L,CS_L):
    for j in range (0,B,CS_B):
        NN=str(ORIGIN)
        JC_X=str(i)
        JC_Y=str((j/Slope)+EC_Ht)
        JC_Z=str(j)
        ORIGIN=ORIGIN+1
        JC1 = (NN + " " + JC_X + " " + JC_Y + " " + JC_Z + ";")
        JC=np.append(JC,JC1)
        NN=str(ORIGIN)
        JC_X=str(i)
        JC_Y=str(0)
        JC_Z=str(j)
        ORIGIN=ORIGIN+1
        JC2 = (NN + " " + JC_X + " " + JC_Y + " " + JC_Z + ";")
        JC=np.append(JC,JC2)
print (JC)