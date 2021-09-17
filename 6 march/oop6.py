
class Base1:
 def __init__(self):
 
  print("inside Base1 constructor")
 def fun(self):
  print("Base1 fun")
  
class Base2:
 def __init__(self):
  print("inside Base2 constructor")
 def fun(self):
   print("Base2 fun")
  
class Derived(Base1,Base2):
 def __init__(self):
  Base1.__init__(self)
  Base2.__init__(self)
  
  print("inside derived constructor")
  
def main():
 dobj = Derived()
 dobj.fun()
 

if __name__== "__main__":
 main()