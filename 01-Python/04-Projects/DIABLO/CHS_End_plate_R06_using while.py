# END PLATE CONNETION FOR CHS WITH FULL CAPACITY
import math as ma
import numpy as np

def chs_end(bd1):
    bdh = bd1 + (1 if bd1<16 else 2 if bd1<=24 else 3)       # Bolt hole
    pen = ma.ceil(bdh*1.2)                               # Bolt end distance
    pp = ma.ceil(bd1*2.5)                                # Bolt pitch distance

    bdet=np.array([[3.6, 4.6, 4.8, 5.6, 5.8, 6.8, 8.8, 8.8, 9.8, 10.9, 12.9],
                   [198, 240, 336, 300, 416, 480, 640, 660, 720, 940, 1100],
                   [330, 400, 420, 500, 520, 600, 800, 830, 900, 1040, 1220]]) #Bolt grade table
    if bg==8.8:
        bye = bdet[1][np.amin(np.where(bdet[0] == bg))+(1 if bd1>16 else 0)] # Bolt yeild strength
        bul = bdet[2][np.amin(np.where(bdet[0] == bg))+(1 if bd1>16 else 0)] # Bolt ultimate strength
    else:
        bye = bdet[1][np.where(bdet[0] == bg)] # Bolt yeild strength
        bul = bdet[2][np.where(bdet[0] == bg)] # Bolt ultimate strength
    plthkav=np.array([6, 8, 10, 12, 16, 20, 25, 32, 40, 45, 50, 
                     55, 60, 65, 70, 75, 80, 85, 90, 95, 100]) # Avaliable plate thickness
    ptk = 6
    pthkf = 0
    while True:
        pdet=np.array([[165, 250, 300, 350, 410, 450, 451], 
                       [165, 250, 300, 350, 410, 450, 450], 
                       [165, 240, 290, 330, 390, 430, 430], 
                       [165, 230, 280, 320, 380, 420, 420], 
                       [290, 410, 440, 490, 540, 570, 590]])    # Plate grade tabke
            
        pul=pdet[4][np.where(pdet[0] == pg)] # Plate ultimate strength
        pye=pdet[1 if ptk<20 else 2 if ptk<=40 else 3][np.where(pdet[0] == pg)]     # Plate yeild strength
 
    #Bolt details
        bsar = ma.pi*bd1**2/4                   # Bolt shank area
        bnar = 0.78*bsar                        # Bolt net area
        bsh = bul*(1*bnar+0*bsar)/(1000*ma.sqrt(3)*1.25)                # Bolt shear strength
        bbr = 2.5*min(pen/(3*bdh), bye/pul, 1)*bd1*ptk*pul/(1000*1.25)  # Bolt bearing strength
        bst = min(bsh, bbr)                                             # Bolt strength
        bten = 0.9*bul*bnar/(1000*1.25)                                 # Bolt tensile strength
        nbreq = max(sh/bst, ax/bten)                                    # No. of bolts required
        nbp = int(ma.ceil((2-nbreq%2)+nbreq))                           # Providing no. of bolts
        btfa = ax/nbp                                                   # Tension force acting per bolt
        # print("\nBolt shear strength D/C ratio : ", round((sh/nbp)/bst, 2),sep='')
        # print("Bolt tensile strength D/C ratio : ", round(btfa/bten, 2),sep='')
        
    #End plate thickness calculation
        pdia = (do+2*(2*pen))+(5-(do+2*(2*pen))%5)      # End plate dia
        ea = (pdia-2*pen-do)/2                          # Eccentricity of bolt from pipe outer dia to bolt centre
        wmom=ma.pi*do/nbp                               # Width of one bolt area (refer D94 in excel)
        epmom=bten*ea*1000                              # Moment in end plate
        epthkreq=ma.sqrt((4*epmom)/(wmom*(pye/1.1)))    # End plate thickness required calculation
        pthkpa = np.abs(plthkav-epthkreq)
        pthkp = np.where(pthkpa==np.amin(pthkpa))
        pthkf = int(plthkav[pthkp])

        if pthkf != ptk:
            ptk = pthkf
        else:
            # print(bd1,nbp,bg,pen,pp,pdia,ptk,pg,sep='\t')
            # re1 = [bd1,nbp,bg,pen,pp,pdia,ptk,pg]
            return bd1, nbp, bg, pen, pp, pdia, ptk, pg
            break


do = 76.1         # Outer dia of pipe
tc = 3.6          # Thickness of pipe
di = do-2*tc      # Inner dia of pipe
ar = ma.pi*(do**2-di**2)/4    # Area of pipe
mom = 6.8         # Moment capacity
sh = 120.0        # Shear capacity
ax = 326.0        # Axial capaciy
bd = np.array([8,10,12,16,20,24,30,36,42])     # Bolt dia
bg = 8.8     # float(input("Enter grade of bolt : "))          # Bolt grade
pg = 350     # int(input("Enter the grade of plate : "))  # For grade E450E enter no. as 451 #End plate grade

re = np.empty((0,8))
for i in bd:
    re = np.append(re,np.array(chs_end(i)))
re = np.reshape(re,(int(np.size(re)/8),8))
print(re,re.ndim,re.shape,re.size,sep='\n\n')
# print('\n\n',re.dtype,'\n')
np.set_printoptions(suppress=True)
ptewt = np.round((ma.pi/4)*7850*((re[:,5]**2)*re[:,6])/(1000**3),2)
# print('\n\n',re[0:][6],'\n')
# print('\n\n',((re[:][5]**2)*re[:][6]),'\n')
# print(ptewt)
re = np.insert(re, 8, ptewt, axis=1)
print(re,re.ndim,re.shape,re.size,sep='\n\n')
# print('\n\n',ptewt.dtype)