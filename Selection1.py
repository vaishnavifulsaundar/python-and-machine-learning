

def checkEven(no):
 if no%2 == 0:
  return True
 else :
  return False


def main():
 print("enter one number")
 value = int(input())
  
 bret = CheckEven(value)

 if bret == True:
  print("{}is Even number".format(value))
 else:
  print ("{}is Odd number".format(value)) 
  

if __name__ == "__main__":
 main()