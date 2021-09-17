# Inbuilt function from module
def Substraction(no1,no2):                  # 100
    return no1 - no2

def SubDecorator(func_name):            # 200       Func_name = 100
    def Updator(a,b):                            # 300
        if a < b: 
            a,b = b,a
        return func_name(a,b)                  # return (call 100(10,6))   -> 4
        
    return Updator                                  # return 300
    
def main():                                            # 400

    sub = SubDecorator(Substraction)      # call 200(100)     sub contains 300
    print("Enter first number")
    value1 = int(input())                           # 6
    print("Enter second number")
    value2 = int(input())                           # 10
    
    ret = sub(value1,value2)                    # call 300(6,10)        4
    
    print("Substraction is",ret)                   # substraction is 4
    
if __name__ == "__main__":
    main()                                                  # call 400
