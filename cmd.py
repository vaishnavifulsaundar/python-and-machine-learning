import sys
print("demonstration of command line arguments")
print("application name:"+sys.argv[0])
x = int(sys.argv[1])
y = int(sys.argv[2])
z = int(x)+int(y)
print(z)