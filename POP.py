def addition(no1,no2):
    ans=0
    ans=no1+no2
    return ans


def subtractino(no1,no2):
    ans=0
    ans=no1-no2
    return ans    

def main():
    num1=int(input("Enter 1st no"))
    num2=int(input("Enter 2nd no"))

    ret=addition(num1, num2)
    print("addtion is : ",ret)

    ret=subtraction(num1, num2)
    print("subtraction is : ",ret)

if __name__=="__main__":
    main()        