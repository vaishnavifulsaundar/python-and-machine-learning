import sys


def main():
 print("recursion limit is:",sys.getrecursionlimit())
 
 sys.setrecursionlimit(1500)
 print(" New recursion limit is:",sys.getrecursionlimit())
 
 
 
 
if __name__ == "__main__":
 main()