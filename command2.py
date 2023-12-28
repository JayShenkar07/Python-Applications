import sys

def main():
    print("Demonstration of command line arguments: ")
    val1=int(sys.argv[1])
    val2=int(sys.argv[2])
    ans=val1+val2
    print("The sum is : ", ans)
if __name__=="__main__":
    main()    

#command python command1.py marvellous 11   