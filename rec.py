
#recursion : calling the function from same function itself


def DisplayIF(no):
 for i in range(no):  #iteration using for loop
  print("hello")
   
def DisplayIW(no):
 while no !=0:
  print("hello")   # iteration using while loop
  no = no-1
   
  
  
  
def DisplayR(no):
 if no != 0:
   no = no-1
   print("hello")
   DisplayR(no)     # recursive call

def main():
 print("enter the number of iterations")
 value = int(input())

 print("calling iterative function with for loop")
 DisplayIF(value)

 print("calling iterative function with for loop")
 DisplayIW(value)

 print("calling recursive function")
 DisplayR(value)


if __name__ == "__main__":
 main()