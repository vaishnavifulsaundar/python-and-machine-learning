Amount = 1000

def ATM(func):
    func()

def Deposit():
    value = int(input("Enter the amount to deposit"))
    global Amount
    Amount = Amount + value
    print("Deposit succesful - Balance : ",Amount)
    
def Withdraw():
    value = int(input("Enter the amount to withdraw"))
    global Amount
    if value > Amount:
        print("There is no sufficeient balance")
    else:
        Amount = Amount - value
        print("Withdraw succesful - Balance : ",Amount)

def main():
    print("Inside main")
    ATM(Deposit)
    ATM(Withdraw)

if __name__ == "__main__":
    main()
