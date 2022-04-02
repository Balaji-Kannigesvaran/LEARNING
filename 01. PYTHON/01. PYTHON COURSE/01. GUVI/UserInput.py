# Getting User Input
# import sys

# x = sys.argv[1]
# y = sys.argv[0]
# z=x+y
# print(z)

def main():
  x,y = input("Enter Two Numbers: ").split(" ")
  z=int(x)+int(y)
  print(z)

if __name__ == "__main__":
  main()