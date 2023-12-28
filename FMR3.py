def add(no1,no2):
    return no1+no2

addX = lambda no1,no2 : no1 + no2 


def checkEven(no): 
    return (no%2==0)

checkEvenX=lambda no : (no%2==0)

def inc(no):
    return no + 2

incX= lambda no : (no+2)

def main():
    # pass    (It is like the virtual function in cpp) 
    ret=add(10,11)
    print(ret)

    ret=checkEven(10)
    print(ret)

    ret=inc(12)
    print(ret)



    ret=addX(10,11)
    print(ret)

    ret=checkEvenX(10)
    print(ret)

    ret=incX(12)
    print(ret)



if __name__=="__main__":
    main()    