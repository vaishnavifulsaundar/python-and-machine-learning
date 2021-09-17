#position arguments
def student(name,rno,address,marks):
  print("name is:",name)
  print("roll number is:",rno)
  print("address is:",address)
  print("marks is:",marks)
  
  #keyword arguments
def computer(RAM,Processor,HDD):
  print("RAM size is",RAM)
  print("processor name is:",Processor)
  print("size of HDD is:",HDD)
  
#default arguments(should be from right to left order)
def CircleArea(radius,PI=3.14):
 print("value of PI is :",PI)
 return PI *radius*radius
 
#variable number of arguments
def fun(*value):
 print("number of arguments are:",len(value))
 
  


def main():
 student("piyush",11,"karve road pune",56)
 
 computer(Processor="i7",RAM=8,HDD="1TB")
 computer(RAM=16,HDD="512GB",Processor="i5")
 
 CircleArea(10.25)
 CircleArea(10.25,7.12)
 fun(10,20,30)
 fun(11,21,51,101,151)
 fun()
 
if __name__== "__main__":
 main()