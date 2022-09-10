# Ceiling
def ceiling(x,s):
    if (x%s==0):return x
    else:return (s+1)*(x/s)
# Floor
def floor(x,s):
    if (x%s==0):return x
    else:return (s)*(x/s)