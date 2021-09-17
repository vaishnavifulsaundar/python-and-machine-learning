def DisplayF(value):
 print("output of for loop")
 inct = 0
 for inct in range(0,value):
  print("jay ganesh")

def DisplayW(value):
 print("output of while loop")
 inct = 0
 while inct < value:
  print("jay ganesh")
  icnt = inct+1

def main():
 print("enter the number of iterations")
 no=int(input())
 
 DisplayF(no)
 DisplayW(no)

if __name__== "__main__":
 main()
 
 #range(start,end,step)
 #start -> starting point of the sequence(inclusive) - Default start is 0
 #end -> Ending point of the sequence(Exclusive)
 #step -> incemnet factor of the sequence - default step is 1