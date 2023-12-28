import marvel

def main():
    val1=int(input("Enter first number"))
    val2=int(input("Enter second number"))
    ans=marvel.Addition(val1, val2)
    print("The answer is ", ans)

    ans=marvel.Subtraction(val1, val2)
    print("The answer is ", ans)

    ans=marvel.Multiplication(val1, val2)
    print("The answer is ", ans)


if __name__ == "__main__":
    main()