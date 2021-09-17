import psutil
from sys import *

def ProcessDisplay():
    print("List of running processess")
    
    Data = []
    
    for proc in psutil.process_iter():
        value = proc.as_dict(attrs = ['pid','name','username'])
        Data.append(value)
        
    return Data
    
def main():
    print("------ Marvellous Infosystems ------")
    print("Script title : "+argv[0])

    arr = ProcessDisplay()
    for element in arr:
        print(element)
        
if __name__ == "__main__":
    main()
