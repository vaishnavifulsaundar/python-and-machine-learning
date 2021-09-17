class Base1:
    def __init__(self):
        print("Inside Base1 constructior")
    def fun(self):
        print("Base1 fun")
        
class Base2:
    def __init__(self):
        print("Inside Base2 constructior")
    def fun(self):
        print("Base2 fun")
        
class Derived(Base2,Base1):
    def __init__(self):
        Base2.__init__(self)
        Base1.__init__(self)
        print("Inside Derived constructor")
    def fun(self):
        print("Derived fun")
        
def main():
    dobj = Derived()
    dobj.fun()
    
if __name__ == "__main__":
    main()
