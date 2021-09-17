class marvellous:
 value1 = 11           #class /static charactristics
 
 def __init__(self,no1,no2):    #constructor
  self.i = no1                  #instance var
  self.j = no2
  print("inside constructor")
 
 def __del__(self):         #destructor
  print("inside destructor")

 def fun(self):            #instance method
  print("inside fun method") 
  print("value of j is",self.j)

def main():
  obj1 = marvellous(11,21)     #creting obj
  obj2 = marvellous(51,101)
 
  print("value of i from obj1",obj1.i)   #accesing instance members
  print("value of i from obj2",obj2.i)
  print("value of class member",marvellous.value1)  #accesing class member
  obj1.fun()                         #calling instance method
  obj2.fun()
  del obj1                           #deallocating the memory of object
  del obj2
if __name__== "__main__":
 main()