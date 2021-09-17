# Inbuilt function from module
def Substraction(no1,no2):
    print("3 : Inside Substraction")
    return no1 - no2

def SubDecorator(func_name):
    print("7 : Inside SubDecorator")
    def Updator(a,b):
        print("9: Inside Updator")
        if a < b:   # first parameter is small
            a,b = b,a
        return func_name(a,b)
        
    return Updator      
    
def main():
    print("17 : Inside main")
    sub = SubDecorator(Substraction)
    print("Enter first number")
    value1 = int(input())
    print("Enter second number")
    value2 = int(input())
    
    ret = sub(value1,value2)
    
    print("Substraction is",ret)
    print("27 : End of main")
    
if __name__ == "__main__":
    print("30 : Inside starter")
    main()
