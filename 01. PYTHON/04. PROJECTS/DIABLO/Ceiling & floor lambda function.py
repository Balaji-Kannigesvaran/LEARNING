ceil = lambda a, b: a + (b - a%b)
floo = lambda a, b: a - a%b
print(ceil(1.45, 0.25)) # a is value, b is the round up value
print(floo(4.95, 0.25)) # a is value, b is the round down value