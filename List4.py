#acpt N numbers from user and return addition of that Nnumbers

def Addition(LIST):
 sum = 0
 for i in range(len(LIST)):
  sum = sum + LIST[i]
 return sum
 

def main():
 arr = []
 print("enter the number of elements")
 size = int(input())
 
 print("enter the elements")
 for i in range(size):
  print("enter the lements no:",i+1)
  value = int(input())
  arr.append(value)
  
 print("Acepted data is:",arr)
 
 ret = Addition(arr)
 
 print("addition of all elements is:",ret)

if __name__== "__main__":
 main()
 
