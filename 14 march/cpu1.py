import os
import time
def Square(no):
 return no * no

def SerialProcessing():
 start = time.time()
 print("serial processing")
 arr = range(10)
 ret=[]
 
 for i in arr:
  ret.append(Square(i))
# print("result of serial processing is",ret)
 end = time.time()
 print("time required for serial execution",end-start)

def main():
 print("inside main")
 SerialProcessing()
 
if __name__== "__main__":
 main()