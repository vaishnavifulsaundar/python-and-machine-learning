def DisplayF(value):
    print("Output of for loop")
    icnt = 0
    for icnt in range(0,value):
        print("Jay Ganesh")

def DisplayW(value):
    print("Output of while loop")
    icnt = 0
    while icnt < value:
        print("Jay Ganesh")
        icnt = icnt + 1
        
def main():
    print("Enter the number of iterations")
    no = int(input())
    
    DisplayF(no)
    DisplayW(no)
    
if __name__ == "__main__":
    main()

# range(   start  ,  end  ,  step)
# start -> Staring point of the sequance (Inclusive) - Default start is 0
# end -> Ending point of the sequance ( Exclusive)
# step -> Incemnet factor of the sequance - default step is 1


# range(1,5,1)      -> 1    2   3   4
# range(1,10,2)    -> 1     3   5   7   9
# range(10)         -> 0    1   2   3   4   5   6   7   8   9
# range(10,1,-1)    -> 10   9   8   7   6   5   4   3   2

# C/ C++/ Java / C#
for(i = 0; i < 10; i++)
{
    // Logic
}

# python
for i in range(0,10,1):         # for i in range(10)
    pass








