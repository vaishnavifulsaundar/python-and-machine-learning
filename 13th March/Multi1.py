import os

def main():
    print("Inside main process")
    
    print("PID of current process is :",os.getpid())
    
    print("PID of parent process is :",os.getppid())
    
if __name__ == "__main__":
    main()
