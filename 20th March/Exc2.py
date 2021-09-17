def main():
    no1 = int(input("Enter first number"))
    no2 = int(input("Enter second number"))
    
    try:
        ans = no1 / no2
    
    except Exception as eobj:
        print("Exception occurs",eobj)
    
    else:
        print("Division is : ",ans)
    
if __name__ == "__main__":
    main()
