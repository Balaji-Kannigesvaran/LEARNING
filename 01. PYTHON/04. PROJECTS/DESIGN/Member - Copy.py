import math as ma
import numpy as np
import pandas as pd

# Member Properties
def memb_prop(L,kz,ky):
    KLz=(L*kz)
    KLy=(L*ky)
    return KLz,KLy

# Material Properties
E=200000
SG='E350'                                                                               # Steel Grade
xls=pd.ExcelFile('D:\Balaji work\PROGRAM\DIABLO\Box Section Diablo.xlsx')               # Reading excel
df=pd.read_excel(xls,"Tables")
df1=df.iloc[5:18,2:7]                                                                   # Reading steel grade table
df1_array=df1.to_numpy()
    
# Section Properties
def chs_sectprop(OuterDia,Thickness):
    D=OuterDia
    t=Thickness
    d=D-2*t                                                                             # inner dia
    fy_sec=df1_array[np.where(df1_array[:,0]==SG)][0][2 if t<20 else 3 if t<=40 else 4] # Yield strength of section
    fu_sec=df1_array[np.where(df1_array[:,0]==SG)][0][1]                                # Ultimate strength of section
    Ag=ma.pi*(D**2-d**2)/4                                                              # Gross area of the section
    An=0.99*Ag                                                                          # Net area of the section
    W=Ag*7850/1E6                                                                       # Wt/m of the section
    I33=ma.pi*(D**4-d**4)/64                                                            # Moment of Inertia of the section
    I22=ma.pi*(D**4-d**4)/64                                                            # Moment of Inertia of the section
    r33=ma.sqrt(I33/Ag)                                                                 # Radius of gyration of the section
    r22=ma.sqrt(I22/Ag)                                                                 # Radius of gyration of the section
    y=D/2
    z=D/2
    S33=I33/y                                                                           # Elastic Section Modulus
    S22=I22/z                                                                           # Elastic Section Modulus
    Z33=(D**3-d**3)/6                                                                   # Plastic Section Modulus
    Z22=(D**3-d**3)/6                                                                   # Plastic Section Modulus
    return D,t,d,fy_sec,fu_sec,Ag,An,W,I33,I22,r33,r22,S33,S22,Z33,Z22

def box_sectprop(Depth,Width,Flange_thickness,Web_thickness):
    D=Depth
    B=Width
    Tf=Flange_thickness
    Tw=Web_thickness
    t=max(Tf,Tw)
    b=B-2*Tw
    d=D-2*Tf                                                                            # inner dia
    fy_sec=df1_array[np.where(df1_array[:,0]==SG)][0][2 if t<20 else 3 if t<=40 else 4] # Yield strength of section
    fu_sec=df1_array[np.where(df1_array[:,0]==SG)][0][1]                                # Ultimate strength of section
    Ag=(B*D)-(b*d)                                                                      # Gross area of the section
    An=0.99*Ag                                                                          # Net area of the section
    W=Ag*7850/1E6                                                                       # Wt/m of the section
    I33=((B*D**3)-(b*d**3))/12                                                          # Moment of Inertia of the section
    I22=((D*B**3)-(d*b**3))/12                                                          # Moment of Inertia of the section
    r33=ma.sqrt(I33/Ag)                                                                 # Radius of gyration of the section
    r22=ma.sqrt(I22/Ag)                                                                 # Radius of gyration of the section
    y=D/2
    z=B/2
    S33=I33/y                                                                           # Elastic Section Modulus  
    S22=I22/z                                                                           # Elastic Section Modulus
    Z33=((B*D**2)-(b*d**2))/4                                                           # Plastic Section Modulus
    Z22=((D*B**2)-(d*b**2))/4                                                           # Plastic Section Modulus
    return D,B,d,b,fy_sec,fu_sec,Ag,An,W,I33,I22,r33,r22,S33,S22,Z33,Z22

#Only for I sections symmetrical about web, Bft and Bfb can vary
def Isec_Sectprop(Depth,Thk_web,Width_TF,Thk_TF,Width_BF,Thk_BF):
    D=Depth
    Bft=Width_TF
    Tft=Thk_TF
    Bfb=Width_BF
    Tfb=Thk_BF
    Tw=Thk_web
    Dw=D-Tft-Tfb
    t=max(Tft,Tfb)
    fy_sec=df1_array[np.where(df1_array[:,0]==SG)][0][2 if t<20 else 3 if t<=40 else 4] # Yield strength of section
    fu_sec=df1_array[np.where(df1_array[:,0]==SG)][0][1]                                # Ultimate strength of section
    Ag=(Bft*Tft)+(Dw*Tw)+(Bfb*Tfb)                                                      # Gross area of the section
    An=0.99*Ag                                                                          # Net area of the section
    W=Ag*7850/1E6                                                                       # Wt/m of the section
    #Moment of Inertia of the section
    a1z=Bft*Tft
    a2z=Dw*Tw
    a3z=Bfb*Tfb
    y1z=Tft/2                                                                           # Y from top
    y2z=Tft+Dw/2
    y3z=Tft+Dw+Tfb/2
    yz=((a1z*y1z)+(a2z*y2z)+(a3z*y3z))/(a1z+a2z+a3z)
    I33=((Bft*Tft**3)/12)+(a1z*((y1z-yz)**2))+((Tw*Dw**3)/12)+(a2z*((y2z-yz)**2))+((Bfb*Tfb**3)/12)+(a3z*((y3z-yz)**2))
    I22=((Tft*Bft**3)/12)+((Dw*Tw**3)/12)+((Tfb*Bfb**3)/12)
    r33=ma.sqrt(I33/Ag)                                                                 # Radius of gyration of the section
    r22=ma.sqrt(I22/Ag)                                                                 # Radius of gyration of the section
    y=D/2
    z=max(Bft,Bfb)/2
    S33=I33/y                                                                           # Elastic Section Modulus  
    S22=I22/z                                                                           # Elastic Section Modulus
    #Plastic Section Modulus
    apy=(((-Bft*Tft)+(Dw*Tw)+(Bfb*Tfb))/(2*Tw))+Tft   
    apz=z
    Z33=(Bft*Tft)*(apy-(Tft/2))+((apy-Tft)*Tw)*((apy-Tft)/2)+((Tft+Dw-apy)*Tw)*((Tft+Dw-apy)/2)+(Bfb*Tfb)*(D-apy-(Tfb/2))
    Z22=((Bft-Tw)/2)*Tft*(Bft/4)+(Dw*Tw/2)*(Tw/4)+((Bfb-Tw)/2)*Tfb*(Bfb/4)                                                           
    return D,Bft,Tft,Bfb,Tfb,Tw,fy_sec,fu_sec,Ag,An,W,I33,I22,r33,r22,S33,S22,Z33,Z22
    
#Only for C sections
def Csec_Sectprop(Depth,Thk_web,Width_TF,Thk_TF,Width_BF,Thk_BF):
    D=Depth
    Bft=Width_TF
    Tft=Thk_TF
    Bfb=Width_BF
    Tfb=Thk_BF
    Tw=Thk_web
    Dw=D-Tft-Tfb
    t=max(Tft,Tfb)
    fy_sec=df1_array[np.where(df1_array[:,0]==SG)][0][2 if t<20 else 3 if t<=40 else 4] # Yield strength of section
    fu_sec=df1_array[np.where(df1_array[:,0]==SG)][0][1]                                # Ultimate strength of section
    Ag=(Bft*Tft)+(Dw*Tw)+(Bfb*Tfb)                                                      # Gross area of the section
    An=0.99*Ag                                                                          # Net area of the section
    W=Ag*7850/1E6                                                                       # Wt/m of the section
    #Moment of Inertia of the section
    a1z=Bft*Tft
    a2z=Dw*Tw
    a3z=Bfb*Tfb
    y1z=Tft/2                                                                           # Y from top
    y2z=Tft+Dw/2
    y3z=Tft+Dw+Tfb/2
    yz=((a1z*y1z)+(a2z*y2z)+(a3z*y3z))/(a1z+a2z+a3z)
    I33=((Bft*Tft**3)/12)+(a1z*((y1z-yz)**2))+((Tw*Dw**3)/12)+(a2z*((y2z-yz)**2))+((Bfb*Tfb**3)/12)+(a3z*((y3z-yz)**2))
    I22=((Tft*Bft**3)/12)+((Dw*Tw**3)/12)+((Tfb*Bfb**3)/12)
    r33=ma.sqrt(I33/Ag)                                                                 # Radius of gyration of the section
    r22=ma.sqrt(I22/Ag)                                                                 # Radius of gyration of the section
    y=D/2
    z=max(Bft,Bfb)/2
    S33=I33/y                                                                           # Elastic Section Modulus  
    S22=I22/z                                                                           # Elastic Section Modulus
    #Plastic Section Modulus
    apy=(((-Bft*Tft)+(Dw*Tw)+(Bfb*Tfb))/(2*Tw))+Tft   
    apz=z
    Z33=(Bft*Tft)*(apy-(Tft/2))+((apy-Tft)*Tw)*((apy-Tft)/2)+((Tft+Dw-apy)*Tw)*((Tft+Dw-apy)/2)+(Bfb*Tfb)*(D-apy-(Tfb/2))
    Z22=((Bft-Tw)/2)*Tft*(Bft/4)+(Dw*Tw/2)*(Tw/4)+((Bfb-Tw)/2)*Tfb*(Bfb/4)                                                           
    return D,Bft,Tft,Bfb,Tfb,Tw,fy_sec,fu_sec,Ag,An,W,I33,I22,r33,r22,S33,S22,Z33,Z22