class Marvellous:
    Value1 = 11                             # Class / Static characteristics
    
    def __init__(self,no1,no2):         # constructor
        self.i = no1                            # instance variable
        self.j = no2
        print("Inside constructor")

    def __del__(self):                      # Destructor
        print("Inside destructor")
        
    def Fun(self):                              # instance method
        print("Inside fun method")
        print("Value of j is",self.j)
        
def main():
    obj1 = Marvellous(11,21)                # Creating the object
    obj2 = Marvellous(51,101)
    print("Value of i from obj1",obj1.i)    # Accessing instance members
    print("Value of i from obj2",obj2.i)
    print("Value of class member",Marvellous.Value1)    # accesing class member
    obj1.Fun()                                      #calling instance method
    obj2.Fun()
    del obj1                                        # deallocating the memory of object
    del obj2
    
if __name__ == "__main__":
    main()
