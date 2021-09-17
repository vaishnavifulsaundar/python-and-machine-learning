import os
import time
import multiprocessing
def Square(no):
 return no * no
 
 ############################################
 
def ParallelProcessing():
 start = time.time()
 print("serial processing")
 arr = range(10000)
 
 pobj = multiprocessing.Pool()
 
 ret =  pobj.map(Square,arr)
 
 
 end = time.time()
 print("time required for parallel execution",end-start)
############################################################

def SerialProcessing():
 start = time.time()
 print("serial processing")
 arr = range(10000)
 ret=[]
 
 for i in arr:
  ret.append(Square(i))
# print("result of serial processing is",ret)
 end = time.time()
 print("time required for serial execution",end-start)
#####################################################################
def main():
 print("inside main")
 SerialProcessing()
 ParallelProcessing()
 
if __name__== "__main__":
 main()