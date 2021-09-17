def substraction(no1,no2):
 return no1 - no2


def subdecorator(fun_name):
 return fun_name(10,5)
 
 
 
 
def main():
 ret = subdecorator(substraction)
 print("substraction is",ret)


if __name__== "__main__":
 main()