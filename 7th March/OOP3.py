class Base:
    def __init__(self):
        self.i = 10
        self.j = 20
        
    def fun(self):
        print("Base fun")

class Derived(Base):
    def __init__(self):
        Base.__init__(self)
        #self.__init__()        Recursive call
        #super().__init__()
        self.x = 30
        self.y = 40

    def gun(self):
        print("Derived gun")
        Base.fun(self)
        self.fun()          # fun(self)
        super().fun()       # fun(self)
        # print(i)
        print(self.i)
        
dobj = Derived()
dobj.gun()
