class Base:
    def __init__(self):
        self.i = 10
        self.j = 20
        print("Inside Base constructior")

    def fun(self):
        print("Inside Base fun")
        
    def gun(self):
        print("Inside Base gun")

class Derived(Base):
    def __init__(self):
        Base.__init__(self)
        self.x = 30
        self.y = 40
        print("Inside Derived constructor")

    def sun(self):
        print("Inside Derived sun")
        
    def gun(self):              # Overriding
        print("Inside Derived gun")

def main():
    bobj = Base()       # Object of base class
    print(bobj.i)
    print(bobj.j)
    bobj.fun()
    bobj.gun()
    
    dobj = Derived()
    print(dobj.i)
    print(dobj.j)
    print(dobj.x)
    print(dobj.y)
    dobj.sun()
    dobj.gun()
    dobj.fun()
    
if __name__ == "__main__":
    main()
