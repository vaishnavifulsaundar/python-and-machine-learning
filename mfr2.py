import functools

def CheckEven(no):
  if(no%2) == 0:
   return True
  else:
   return False
  
def Increment(no):
 return no +2
 
def Add(no1,no2):
 return no1 + no2
  
  

def main():
 arr = []
 print("enter number of elements")
 size=int(input())
 
 for i in range(size):
  print("enter element number:",i+1)
  no = int(input())
  arr.append(no)
  
 print("your entered data is:",arr)
  #newdata = filter(fun_name , data)
 newdata = list(filter(CheckEven,arr))    #newdata = MarvellousFilter(arr)
 print("after filtering data is:",newdata)
 
 newdata1 = list(map(Increment,newdata))   #newdata1 = MarvellousMap(newdata)
 print("after map data is:",newdata1)
 
 output = functools.reduce(Add,newdata1)   # output = MarvellousReduce(newdata1)
 print("after reduce result is:",output)
 
 
if __name__== "__main__":
 main()