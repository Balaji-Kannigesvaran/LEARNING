letters=['A','B','C','D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers=['0','1','2','3','4','5','6','7','8','9']

def alphanumericpresece(start,end,ip_str):
  sttyplist=[]
  stposlist=[]
  endtyplist=[]
  endposlist=[]
  for i in start:
    stpostyp = letters if(i in letters) else numbers
    stpos=stpostyp.index(i)
    sttyplist.append(stpostyp)
    stposlist.append(stpos)
  for i in end:
    endpostyp = letters if(i in letters) else numbers
    endpos=endpostyp.index(i)
    endtyplist.append(endpostyp)
    endposlist.append(endpos)
  aplhanumlist=[]
  for p0 in range(stposlist[0],endposlist[0]+1):
    for p1 in range(stposlist[1],endposlist[1]+1):
      for p2 in range(stposlist[2],endposlist[2]+1):
        aplhanumstr=sttyplist[0][p0]+sttyplist[1][p1]+sttyplist[2][p2]
        aplhanumlist.append(aplhanumstr)
  # print(aplhanumlist)
  if ip_str in aplhanumlist:
    print("It is within the range 👍")
  else:
    print("Out of range 👎")

alphanumericpresece("A1A","H9Z","D5F")

# if ((ord('D5F')>=ord('A1A')) and (ord('D5F')<=ord('H9Z'))):
#   print ('Within Range')