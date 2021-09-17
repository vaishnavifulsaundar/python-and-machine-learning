import threading
Amount = 1000

def ATM(func):
 func()


def Deposit():
 value = int(input("Enter amount to deposit"))
 global Amount
 Amount = Amount + value
 print("Deposit successful - Balance:",Amount)


def Withdraw():
 value = int(input("enter the amount to withdraw"))
 global Amount
 if value > Amount:
  print("there is no sufficient balance")
 else:
  Amount = Amount - value
  print("withdraw successful - Balance:",Amount)


def main():
 print("inside main")
 ATM(Deposit)
 ATM(Withdraw)


if __name__== "__main__":
 main()