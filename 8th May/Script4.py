import os
import time
import psutil
from sys import *

def ProcessDisplay(FolderName = "Marvellous"):
    
    Data = []
    
    if not os.path.exists(FolderName):
        os.mkdir(FolderName)
    else:
        print("Destination directory is already present")
        exit()
        
    return
    
    for proc in psutil.process_iter():
        value = proc.as_dict(attrs = ['pid','name','username'])
        Data.append(value)
        
    return Data
    
def main():
    print("------ Marvellous Infosystems ------")
    print("Script title : "+argv[0])

    if(len(argv) != 2):
        print("Insufficient arguments")
        exit()
    
    if(argv[1] == "-u") or (argv[1] == "-U"):
        print("Usage : Application_Name Directory_Name")
        exit()
        
    if(argv[1] == "-h") or (argv[1] == "-H"):
        print("Help : It is used to create log file of running processess")
        exit()
            
    ProcessDisplay(argv[1])
    
if __name__ == "__main__":
    main()
