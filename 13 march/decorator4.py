#inbuilt function from module

def substraction(no1,no2):    #100
 return no1 - no2

def subdecorator(fun_name):  #200    fun_name = 100
 def updator(a,b):           #300
  if a < b:                  #first parameter is small
  
   a,b = b,a
  
  return fun_name(a,b)     #return(call 100(10,6)) ->4
  
 return updator           #return 300
 
def main():                 #400
 sub = subdecorator(substraction)     #call 200(100)   sub contains 300
 print("enter 1st number")
 value1 = int(input())       #6
 print("enter 2nd number")
 value2 = int(input())       #10
  
 ret = sub(value1,value2)    #call 300(6,10) ->4
 
 print("substraction is",ret)  #substraction is 4
 

if __name__== "__main__":
 main()                   #call 400