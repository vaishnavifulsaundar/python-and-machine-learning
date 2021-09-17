def Addition(LIST):
 sum = 0
 for i in range(len(LIST)):
  sum = sum + LIST[i]
 return sum
 
def main():
 arr = []
 print("enter the number of elements")
 size = int(input())
 
 for i in range(size):
  print("enter the element no:",i+1)
  value = int(input())
  arr.append(value)
  
 print("Accepted data is:",arr)
 
 ret = Addition(arr)
 
 print("addition of all elemets:",ret)
 
if __name__== "__main__":
 main()