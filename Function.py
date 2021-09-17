# Positional arguments
def Student(name,rno,address,marks):
    print("Name is :",name)
    print("Roll number is :",rno)
    print("Address is :",address)
    print("Marks is :",marks)

# Keyword Arguments
def Computer(RAM,Processor,HDD):
    print("RAM size is ",RAM)
    print("Processor name is ",Processor)
    print("Size of HDD is ",HDD)
    
# default argument (Should be from Right to left order)
def CicleArea(Radious, PI= 3.14):
    print("Value of PI is : ",PI)
    return PI * Radious * Radious
    
#Variable number of arguments
def Fun(*Value):
    print(type(Value))
    print("Number of arguments are : ",len(Value))
    
def main():
    Student("Piyush",11,"Karve road Pune",56)
    
    Computer(Processor="i7",RAM=8,HDD="1TB")
    Computer(RAM=16,HDD="512GB",Processor="i5")
    
    CicleArea(10.25)
    CicleArea(Radious=10.25,PI = 7.12)
    
    Fun(10,20,30)
    Fun(11,21,51,101,151)
    Fun()
    
if __name__ == "__main__":
    main()
