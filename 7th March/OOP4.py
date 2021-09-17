class Base:
    def __init__(self):
        self.i =10
        
    def fun(self):
        print("Base fun")

class Derived(Base):
    def __init__(self):
        Base.__init__(self)
        self.i =20
        
    def fun(self):
        print("Derived fun")

    def gun(self):
        print("Derived gun")
        self.fun()
        super().fun()
        print(Base().i)
        print(self.i)
        
dobj = Derived()
dobj.gun()
