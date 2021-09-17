

#iterative approach
def StartDynamic(No,message="Jay ganesh"):
 icnt = 0
 while icnt<No:
  print(message)
  icnt = icnt + 1

def Display(No):
 print("Jay Ganesh"*No)
 

def main():
 print("Enter number of times you want to display message on screen")
 value = int(input())
 print("enter the message")
 name = input()
 
 StartDynamic(value,name)
 
 StartDynamic(value)
 
 Display(value)


if __name__== "__main__":
 main()