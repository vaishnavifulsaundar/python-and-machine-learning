def CheckEven(no):
  if no %2 == 0:
   return True
  else:
   return False
   
   
def MarvellousFilter(arr):
 brr = []
 for i in range(len(arr)):
  if CheckEven(arr[i]) == True:
    brr.append(arr[i])
   
 return brr

def MarvellousMap(arr):
 for i in range(len(arr)):
  arr[i] = arr[i] + 2
  
 return arr
 
 
def MarvellousReduce(arr):
 sum = 0
 for i in range(len(arr)):
  sum = sum +arr[i]
 return sum



def main():
 arr = []
 print("enter number of elements")
 size=int(input())
 
 for i in range(size):
  print("enter element number:",i+1)
  no = int(input())
  arr.append(no)
  
 print("your entered data is:",arr)
 newdata = MarvellousFilter(arr)
 print("after filtering data is:",newdata)
 
 newdata1 = MarvellousMap(newdata)
 print("after map data is:",newdata1)
 
 output = MarvellousReduce(newdata1)
 print("after reduce result is:",output)
 
 
if __name__== "__main__":
 main()