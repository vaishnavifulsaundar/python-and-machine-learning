def main():
    name = input("Enter the file name")
    
    fobj = open(name,"r")
    
    print("single line from file is ")
    print(fobj.readline())
    
if __name__ == "__main__":
    main()
