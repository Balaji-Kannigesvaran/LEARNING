from regex import A


str1 = "This is a python interview"

set1 = set (str1)
for i in set1:
  li=[]
  for j in range (len(str1)):
    if i == j:
      print (j)
      a = (str1.index(j))
      li.append(a)
      print(li)
      print(len(li))

a = frozenset([1,5,"python"])

