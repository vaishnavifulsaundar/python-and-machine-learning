def main():
    name = input("Enter the file name that you want to create")
    
    fobj = open(name,"w")   # create new file
    
    str = input("Enter the data that you want to write in the file")
    
    fobj.write(str)
    
if __name__ == "__main__":
    main()
