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
SG='E350'                                                                                # Steel Grade
xls=pd.ExcelFile('D:\Balaji work\PROGRAM\DIABLO\Box Section Diablo.xlsx')                # Reading excel
df=pd.read_excel(xls,"Tables")
df1=df.iloc[5:18,2:7]                                                                    # Reading steel grade table
df1_array=df1.to_numpy()
    
# Section Properties
def chs_sectprop(OuterDia,Thickness):
    D=OuterDia
    t=Thickness
    d=D-2*t                                                                              # inner dia
    fy_sec=df1_array[np.where(df1_array[:,0]==SG)][0][2 if t<20 else 3 if t<=40 else 4]  # Yield strength of section
    fu_sec=df1_array[np.where(df1_array[:,0]==SG)][0][1]                                 # Ultimate strength of section
    Ag=ma.pi*(D**2-d**2)/4                                                               # Gross area of the section
    An=0.99*Ag                                                                           # Net area of the section
    W=Ag*7850/1E6                                                                        # Wt/m of the section
    Profile=('CHS '+str(D)+'X'+str(t)+' - '+str(round(W,0)))
    I33=ma.pi*(D**4-d**4)/64                                                             # Moment of Inertia of the section
    I22=ma.pi*(D**4-d**4)/64                                                             # Moment of Inertia of the section
    r33=ma.sqrt(I33/Ag)                                                                  # Radius of gyration of the section
    r22=ma.sqrt(I22/Ag)                                                                  # Radius of gyration of the section
    # Elastic Section Modulus
    y=D/2
    z=D/2
    S33P=I33/y
    S33N=I33/(D-y)
    S22P=I22/z
    S22N=I22/(D-z)                                                                        
    Z33=(D**3-d**3)/6                                                                    # Plastic Section Modulus
    Z22=(D**3-d**3)/6                                                                    # Plastic Section Modulus
    return Profile,D,t,d,fy_sec,fu_sec,Ag,An,W,I33,I22,r33,r22,S33P,S33N,S22P,S22N,Z33,Z22

def box_sectprop(Depth,Width,Flange_thickness,Web_thickness):
    D=Depth
    B=Width
    Tf=Flange_thickness
    Tw=Web_thickness
    t=max(Tf,Tw)
    b=B-2*Tw
    d=D-2*Tf            
    fy_sec=df1_array[np.where(df1_array[:,0]==SG)][0][2 if t<20 else 3 if t<=40 else 4]  # Yield strength of section
    fu_sec=df1_array[np.where(df1_array[:,0]==SG)][0][1]                                 # Ultimate strength of section
    Ag=(B*D)-(b*d)                                                                       # Gross area of the section
    An=0.99*Ag                                                                           # Net area of the section
    W=Ag*7850/1E6                                                                        # Wt/m of the section
    Profile=(('SHS ' if B==D else 'RHS ')+str(D)+'X'+str(B)+'X'+str(Tf)+'X'+str(Tw)+' - '+str(round(W,0))) 
    I33=((B*D**3)-(b*d**3))/12                                                           # Moment of Inertia of the section
    I22=((D*B**3)-(d*b**3))/12                                                           # Moment of Inertia of the section
    r33=ma.sqrt(I33/Ag)                                                                  # Radius of gyration of the section
    r22=ma.sqrt(I22/Ag)                                                                  # Radius of gyration of the section
    # Elastic Section Modulus
    y=D/2
    z=B/2
    S33P=I33/y
    S33N=I33/(D-y)                                                                          
    S22P=I22/z
    S22N=I22/(B-z)                                                                        
    Z33=((B*D**2)-(b*d**2))/4                                                            # Plastic Section Modulus
    Z22=((D*B**2)-(d*b**2))/4                                                            # Plastic Section Modulus
    return Profile,D,B,d,b,fy_sec,fu_sec,Ag,An,W,I33,I22,r33,r22,S33P,S33N,S22P,S22N,Z33,Z22

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
    fy_sec=df1_array[np.where(df1_array[:,0]==SG)][0][2 if t<20 else 3 if t<=40 else 4]  # Yield strength of section
    fu_sec=df1_array[np.where(df1_array[:,0]==SG)][0][1]                                 # Ultimate strength of section
    Ag=(Bft*Tft)+(Dw*Tw)+(Bfb*Tfb)                                                       # Gross area of the section
    An=0.99*Ag                                                                           # Net area of the section
    W=Ag*7850/1E6                                                                        # Wt/m of the section
    Profile=('BU '+str(D)+'X'+(str(Bft) if Bft==Bfb else str(Bft)+'('+str(Bfb)+')')+'X'+(str(Tft) if Tft==Tfb else str(Tft)+'('+str(Tfb)+')')+'X'+str(Tw)+' - '+str(round(W,0)))
    #Moment of Inertia of the section
    a1=Bft*Tft
    a2=Dw*Tw
    a3=Bfb*Tfb
    y1=Tft/2                                                                             # Y from top
    y2=Tft+Dw/2
    y3=Tft+Dw+Tfb/2
    yz=((a1*y1)+(a2*y2)+(a3*y3))/(a1+a2+a3)
    zy=max(Bft,Bfb)/2
    I33=((Bft*Tft**3)/12)+(a1*((y1-yz)**2))+((Tw*Dw**3)/12)+(a2*((y2-yz)**2))+((Bfb*Tfb**3)/12)+(a3*((y3-yz)**2))
    I22=((Tft*Bft**3)/12)+((Dw*Tw**3)/12)+((Tfb*Bfb**3)/12)
    r33=ma.sqrt(I33/Ag)                                                                  # Radius of gyration of the section
    r22=ma.sqrt(I22/Ag)                                                                  # Radius of gyration of the section
    # Elastic Section Modulus
    S33P=I33/yz             
    S33N=I33/(D-yz)
    S22P=I22/zy       
    S22N=I22/(max(Bft,Bfb)-zy)                                                                       
    #Plastic Section Modulus
    apy=(((-Bft*Tft)+(Dw*Tw)+(Bfb*Tfb))/(2*Tw))+Tft   
    apz=zy
    Z33=((Bft*Tft)*(apy-(Tft/2)))+(((apy-Tft)*Tw)*((apy-Tft)/2))+(((Tft+Dw-apy)*Tw)*((Tft+Dw-apy)/2))+((Bfb*Tfb)*(D-apy-(Tfb/2)))
    Z22=(((Bft-Tw)/2)*Tft*(((Bft-Tw)/2/2)+(Tw/2))+(D*Tw/2)*(Tw/4)+((Bfb-Tw)/2)*Tfb*(((Bfb-Tw)/2/2)+(Tw/2)))*2                                                          
    return Profile,D,Bft,Tft,Bfb,Tfb,Tw,fy_sec,fu_sec,Ag,An,W,I33,I22,r33,r22,S33P,S33N,S22P,S22N,Z33,Z22

#Only for H sections symmetrical about web, Bft and Bfb can vary
def Hsec_Sectprop(Depth,Thk_web,Width_TF,Thk_TF,Width_BF,Thk_BF):
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
    Profile=('BU '+str(D)+'X'+(str(Bft) if Bft==Bfb else str(Bft)+'('+str(Bfb)+')')+'X'+(str(Tft) if Tft==Tfb else str(Tft)+'('+str(Tfb)+')')+'X'+str(Tw)+' - '+str(round(W,0)))
    #Moment of Inertia of the section
    a1=Bft*Tft
    a2=Dw*Tw
    a3=Bfb*Tfb
    z1=Tft/2                                                                            # Z from left
    z2=Tft+Dw/2
    z3=Tft+Dw+Tfb/2
    zy=((a1*z1)+(a2*z2)+(a3*z3))/(a1+a2+a3)
    yz=max(Bft,Bfb)/2
    I33=((Tft*Bft**3)/12)+((Dw*Tw**3)/12)+((Tfb*Bfb**3)/12)
    I22=((Bft*Tft**3)/12)+(a1*((z1-zy)**2))+((Tw*Dw**3)/12)+(a2*((z2-zy)**2))+((Bfb*Tfb**3)/12)+(a3*((z3-zy)**2))
    r33=ma.sqrt(I33/Ag)                                                                 # Radius of gyration of the section
    r22=ma.sqrt(I22/Ag)                                                                 # Radius of gyration of the section
    # Elastic Section Modulus
    S33P=I33/yz             
    S33N=I33/(max(Bft,Bfb)-yz)
    S22P=I22/zy       
    S22N=I22/(D-zy)
    #Plastic Section Modulus
    apy=zy
    apz=(((-Bft*Tft)+(Dw*Tw)+(Bfb*Tfb))/(2*Tw))+Tft   
    Z33=(((Bft-Tw)/2)*Tft*(((Bft-Tw)/2/2)+(Tw/2))+(D*Tw/2)*(Tw/4)+((Bfb-Tw)/2)*Tfb*(((Bfb-Tw)/2/2)+(Tw/2)))*2                                                          
    Z22=(Bft*Tft)*(apz-(Tft/2))+((apz-Tft)*Tw)*((apz-Tft)/2)+((Tft+Dw-apz)*Tw)*((Tft+Dw-apz)/2)+(Bfb*Tfb)*(D-apz-(Tfb/2))
    return Profile,D,Bft,Tft,Bfb,Tfb,Tw,fy_sec,fu_sec,Ag,An,W,I33,I22,r33,r22,S33P,S33N,S22P,S22N,Z33,Z22
    
#Only for C sec
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
    Profile=('BU '+str(D)+'X'+(str(Bft) if Bft==Bfb else str(Bft)+'('+str(Bfb)+')')+'X'+(str(Tft) if Tft==Tfb else str(Tft)+'('+str(Tfb)+')')+'X'+str(Tw)+' - '+str(round(W,0)))
    #Moment of Inertia of the section
    a1=Bft*Tft
    a2=Dw*Tw
    a3=Bfb*Tfb
    y1=Tft/2                                                                           # Y from top
    y2=Tft+Dw/2
    y3=Tft+Dw+Tfb/2
    yz=((a1*y1)+(a2*y2)+(a3*y3))/(a1+a2+a3)
    z1=Bft/2                                                                           # Z from left
    z2=Tw/2
    z3=Bfb/2
    zy=((a1*z1)+(a2*z2)+(a3*z3))/(a1+a2+a3)                  
    I33=((Bft*Tft**3)/12)+(a1*((y1-yz)**2))+((Tw*Dw**3)/12)+(a2*((y2-yz)**2))+((Bfb*Tfb**3)/12)+(a3*((y3-yz)**2))
    I22=((Tft*Bft**3)/12)+(a1*((z1-zy)**2))+((Dw*Tw**3)/12)+(a2*((z2-zy)**2))+((Tfb*Bfb**3)/12)+(a3*((z3-zy)**2))
    r33=ma.sqrt(I33/Ag)                                                                # Radius of gyration of the section
    r22=ma.sqrt(I22/Ag)                                                                # Radius of gyration of the section
    # Elastic Section Modulus
    S33P=I33/yz
    S33N=I33/(D-yz)                                                                       
    S22P=I22/zy
    S22N=I22/(max(Bft,Bfb)-zy)           
    #Plastic Section Modulus
    apy=(((-Bft*Tft)+(Dw*Tw)+(Bfb*Tfb))/(2*Tw))+Tft   
    apz=((Bft*Tft)-(Dw*Tw)+(Bfb*Tfb))/((2*Tft)+(2*Tfb))
    Z33=(Bft*Tft)*(apy-(Tft/2))+((apy-Tft)*Tw)*((apy-Tft)/2)+((Tft+Dw-apy)*Tw)*((Tft+Dw-apy)/2)+(Bfb*Tfb)*(D-apy-(Tfb/2))
    Z22=((apz*Tft)*(apz/2))+(((Bft-apz)*Tft)*(Bft-apz)/2)+((Dw*Tw)*(apz-Tw/2))+((apz*Tfb)*(apz/2))+(((Bfb-apz)*Tfb)*(Bfb-apz)/2)                                                            
    return Profile,D,Bft,Tft,Bfb,Tfb,Tw,fy_sec,fu_sec,Ag,An,W,I33,I22,r33,r22,S33P,S33N,S22P,S22N,Z33,Z22

#Only for Inverted C sec
def InvCsec_Sectprop(Depth,Thk_web,Width_TF,Thk_TF,Width_BF,Thk_BF):
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
    Profile=('BU '+str(D)+'X'+(str(Bft) if Bft==Bfb else str(Bft)+'('+str(Bfb)+')')+'X'+(str(Tft) if Tft==Tfb else str(Tft)+'('+str(Tfb)+')')+'X'+str(Tw)+' - '+str(round(W,0)))
    #Moment of Inertia of the section
    a1=Bft*Tft
    a2=Dw*Tw
    a3=Bfb*Tfb
    y1=Tft/2                                                                           # Y from top
    y2=Tft+Dw/2
    y3=Tft+Dw+Tfb/2
    yz=((a1*y1)+(a2*y2)+(a3*y3))/(a1+a2+a3)
    z1=Bft/2                                                                           #Z from left
    z2=max(Bft,Bfb)-Tw/2
    z3=Bfb/2
    zy=((a1*z1)+(a2*z2)+(a3*z3))/(a1+a2+a3)                  
    I33=((Bft*Tft**3)/12)+(a1*((y1-yz)**2))+((Tw*Dw**3)/12)+(a2*((y2-yz)**2))+((Bfb*Tfb**3)/12)+(a3*((y3-yz)**2))
    I22=((Tft*Bft**3)/12)+(a1*((z1-zy)**2))+((Dw*Tw**3)/12)+(a2*((z2-zy)**2))+((Tfb*Bfb**3)/12)+(a3*((z3-zy)**2))
    r33=ma.sqrt(I33/Ag)                                                                # Radius of gyration of the section
    r22=ma.sqrt(I22/Ag)                                                                # Radius of gyration of the section
    # Elastic Section Modulus
    S33P=I33/yz
    S33N=I33/(D-yz)                                                                       
    S22P=I22/zy
    S22N=I22/(max(Bft,Bfb)-zy)           
    #Plastic Section Modulus
    apy=(((-Bft*Tft)+(Dw*Tw)+(Bfb*Tfb))/(2*Tw))+Tft   
    apz=max(Bft,Bfb)-(((Bft*Tft)-(Dw*Tw)+(Bfb*Tfb))/((2*Tft)+(2*Tfb)))
    Z33=(Bft*Tft)*(apy-(Tft/2))+((apy-Tft)*Tw)*((apy-Tft)/2)+((Tft+Dw-apy)*Tw)*((Tft+Dw-apy)/2)+(Bfb*Tfb)*(D-apy-(Tfb/2))
    Z22=((apz*Tft)*(apz/2))+(((Bft-apz)*Tft)*(Bft-apz)/2)+((Dw*Tw)*(apz-Tw/2))+((apz*Tfb)*(apz/2))+(((Bfb-apz)*Tfb)*(Bfb-apz)/2)                                                            
    return Profile,D,Bft,Tft,Bfb,Tfb,Tw,fy_sec,fu_sec,Ag,An,W,I33,I22,r33,r22,S33P,S33N,S22P,S22N,Z33,Z22

