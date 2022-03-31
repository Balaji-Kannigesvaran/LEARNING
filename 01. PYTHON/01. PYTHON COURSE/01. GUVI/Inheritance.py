class A:
    def feature1(self):
        print ("Feature1 in A is working")
    def feature2(self):
        print ("Feature2 in A is working")
class B():
    def feature2(self):
        print ("Feature2 in B is working")
    def feature3(self):
        print ("Feature3 in B is working")
class C(A,B):
    def feature2(self):
        super().feature2()
        print("feature 2 in C is working")

c1=C()
c1.feature2()
