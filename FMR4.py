from functools import reduce

checkEven = lambda no : no%2==0

inc=  lambda no : no+2

add = lambda a,b: a+b


def main():
    data=[]
    print("Enter the number of elements: ")
    size=int(input())

    for i in range(0,size):
        item=int(input())
        data.append(item)

    print("Elements are accepted successfully! ")

    print()
    print(data)
    output=list(filter(checkEven, data))
    print("Output after Filter ", output)
    moutput=list(map(inc, output))
    print("Output after Map ", moutput)

    result=reduce(add,moutput)
    print("Output after Reduce ", result)



if __name__=="__main__":
    main()


    #Filter Map Reduce is an important concept for interviews: 