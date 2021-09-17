#iterative approach
def StartDynamic(No):
 icnt = 0
 while icnt<No:
  print("Jay Ganesh")
  icnt = icnt + 1
  
  
  
def main():
 print("Enter number of times you want to display message on screen")
 value = int(input())
 
 StartDynamic(value)
 
if __name__== "__main__":
 main()