class Base:
 def __init__(self):
  self.i = 10
  self.j = 20
  
 def fun(self):
  print("public fun")
  
class Derived(Base):
 def __init__(self):
  Base.__init__(self)
  #self.__init__()    recursive call
  #super().__init__()
  
  self.x =30
  self.y = 40
  
 def gun(self):
  print("derived gun")
  Base.fun(self)         #fun(self)
  self.fun()             #fun(self)
  super().fun()
  #print(i)
  print(self.i)
  print(super().i)
  
dobj = Derived()
dobj.gun()