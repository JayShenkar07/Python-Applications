from functools import reduce

def checkEven(no):
    if(no%2==0):
        return True
    else:
        return False

def inc(no):
    return no+2


def add(a,b):
    return a+b


def main():
    data=[5,4,9,8,13,17,12,18]

    print(data)
    output=list(filter(checkEven, data))
    print(output)
    moutput=list(map(inc, output))
    print(moutput)

    result=reduce(add,moutput)
    print(result)



if __name__=="__main__":
    main()