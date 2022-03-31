import Member as me

# Profile,D,B,d,b,fy_sec,fu_sec,Ag,An,W,I33,I22,r33,r22,S33P,S33N,S22P,S22N,Z33,Z22=me.box_sectprop(225,225,10,10)
# print (Profile,'\n',D,B,d,b,'\n',fy_sec,fu_sec,Ag,An,W,'\n',I33,I22,r33,r22,'\n',S33P,S33N,'\n',S22P,S22N,'\n',Z33,Z22,'\n')

# Profile,D,t,d,fy_sec,fu_sec,Ag,An,W,I33,I22,r33,r22,S33P,S33N,S22P,S22N,Z33,Z22=me.chs_sectprop(114.3, 5.4)
# print (Profile,'\n',D,t,d,'\n',fy_sec,fu_sec,Ag,An,W,'\n',I33,I22,r33,r22,'\n',S33P,S33N,'\n',S22P,S22N,'\n',Z33,Z22,'\n')

# Profile,D,Bft,Tft,Bfb,Tfb,Tw,fy_sec,fu_sec,Ag,An,W,I33,I22,r33,r22,S33P,S33N,S22P,S22N,Z33,Z22=me.Isec_Sectprop(350, 12, 250, 12, 300, 25)
# print (Profile,'\n',D,Bft,Tft,Bfb,Tfb,Tw,'\n',fy_sec,fu_sec,Ag,An,W,'\n',I33,I22,r33,r22,'\n',S33P,S33N,'\n',S22P,S22N,'\n',Z33,Z22,'\n')

# Profile,D,Bft,Tft,Bfb,Tfb,Tw,fy_sec,fu_sec,Ag,An,W,I33,I22,r33,r22,S33P,S33N,S22P,S22N,Z33,Z22=me.Hsec_Sectprop(350, 12, 250, 12, 300, 25)
# print (Profile,'\n',D,Bft,Tft,Bfb,Tfb,Tw,'\n',fy_sec,fu_sec,Ag,An,W,'\n',I33,I22,r33,r22,'\n',S33P,S33N,'\n',S22P,S22N,'\n',Z33,Z22,'\n')

Profile,D,Bft,Tft,Bfb,Tfb,Tw,fy_sec,fu_sec,Ag,An,W,I33,I22,r33,r22,S33P,S33N,S22P,S22N,Z33,Z22=me.Csec_Sectprop(300, 6, 75, 16, 75, 16)
print (Profile,'\n',D,Bft,Tft,Bfb,Tfb,Tw,'\n',fy_sec,fu_sec,Ag,An,W,'\n',I33,I22,r33,r22,'\n',S33P,S33N,'\n',S22P,S22N,'\n',Z33,Z22,'\n')

Profile,D,Bft,Tft,Bfb,Tfb,Tw,fy_sec,fu_sec,Ag,An,W,I33,I22,r33,r22,S33P,S33N,S22P,S22N,Z33,Z22=me.InvCsec_Sectprop(300, 6, 75, 16, 75, 16)
print (Profile,'\n',D,Bft,Tft,Bfb,Tfb,Tw,'\n',fy_sec,fu_sec,Ag,An,W,'\n',I33,I22,r33,r22,'\n',S33P,S33N,'\n',S22P,S22N,'\n',Z33,Z22,'\n')
