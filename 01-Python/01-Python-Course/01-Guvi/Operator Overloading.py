class Student:
  def __init__ (self,m1,m2):
    self.m1=m1
    self.m2=m2
  def __add__ (self,other):
    m1=self.m1+other.m1
    m2=self.m2+other.m2
    total = Student(m1,m2)
    return total
  def __str__(self):
    return '{} {} '.format(self.m1,self.m2)

s1=Student(40,50)
s2=Student(60,70)

total=s1+s2
print(total)
print(total.m1)
print(total.m2)