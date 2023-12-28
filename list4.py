def main():
    print("Enter number of elements to be stored:  ")
    length=int(input())
    arr=list()  #creating an empty list 
    #this list() function is actually an object as python is object based language
    print("Enter your elements: ")
    for i in range(length):
        value=int(input())
        arr.append(value)

    #displaying the elements
    print("Elements from the list are ")
    for i in range(length):
        print(arr[i], end=" ")

    else:
        print(" ")
        print("Program Terminated successfully !!")
if __name__ == "__main__":
    main()    