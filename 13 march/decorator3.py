#inbuilt function from module

def substraction(no1,no2):
 print("4:inside substraction")

 return no1 - no2

def subdecorator(fun_name):
 print("7:inside subdecorator")
 def updator(a,b):
  print("9:inside updator")
  if a < b:                  #first parameter is small
   
   a,b = b,a
  
  return fun_name(a,b)
  
 return updator
 
def main():
 print("21:inside main")
 sub = subdecorator(substraction)
 print("enter 1st number")
 value1 = int(input())
 print("enter 2nd number")
 value2 = int(input())
 ret = sub(value1,value2)
 print("substraction is",ret)
 print("27:end of main")
 

if __name__== "__main__":
 print("31:inside starter")
 main()