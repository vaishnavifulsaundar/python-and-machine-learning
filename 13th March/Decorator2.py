# Inbuilt function from module
def Substraction(no1,no2):
    return no1 - no2

def SubDecorator(func_name):
    def Updator(a,b):
        if a < b:   # first parameter is small
            a,b = b,a
        return func_name(a,b)
        
    return Updator
    
def main():

    sub = SubDecorator(Substraction)
    print("Enter first number")
    value1 = int(input())
    print("Enter second number")
    value2 = int(input())
    
    ret = sub(value1,value2)
    
    print("Substraction is",ret)
    
if __name__ == "__main__":
    main()
