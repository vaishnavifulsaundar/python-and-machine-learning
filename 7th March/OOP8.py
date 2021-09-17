class Demo:
    def __init__(self,no1,no2):
        self.no1 = no1
        self.no2 = no2
        
    def Add(self):
        return self.no1+self.no2

def main():
    print("Enter first number")
    x = int(input())
    print("Enter second number")
    y = int(input())
    
    obj = Demo(x,y)
    ret = obj.Add()
    print("Addition is",ret)
    
if __name__ == "__main__":
    main()
 
