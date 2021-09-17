#inbuilt function from module

def substraction(no1,no2):
 return no1 - no2


def subdecorator(fun_name):
 def updator(a,b):
  if a < b:  #first parameter is small
   '''''temp = a
   a = b
   b = temp'''''
   a,b = b,a
  
  return fun_name(a,b)
  
 return updator
 
 
 
 
def main():
 sub = subdecorator(substraction)
 print("enter 1st number")
 value1 = int(input())
 print("enter 2nd number")
 value2 = int(input())
 ret = sub(value1,value2)
 print("substraction is",ret)
 

if __name__== "__main__":
 main()