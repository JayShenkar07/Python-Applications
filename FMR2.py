from functools import reduce

def checkEven(no):
    return (no%2==0)

def inc(no):
    return no+2


def add(a,b):
    return a+b


def main():
    data=[]
    print("Enter the number of elements: ")
    size=int(input())

    for i in range(0,size):
        item=int(input())
        data.append(item)

    print("Elements are accepted successfully! ")

    print(data)
    output=list(filter(checkEven, data))
    print(output)
    moutput=list(map(inc, output))
    print(moutput)

    result=reduce(add,moutput)
    print(result)



if __name__=="__main__":
    main()


    #Filter Map Reduce is an important concept for interviews: 