class chs:
  def inputDimensions (self):
    print("Diameter")
    print("Thickness")

class rhs:
  def inputDimensions (self):
    print("Depth")
    print("Width")
    print("Thickness")

class inputs:
  def inputsReqd(self,shape):
    shape.inputDimensions()

shape = rhs()
inputsfromuser = inputs()
inputsfromuser.inputsReqd(shape)
