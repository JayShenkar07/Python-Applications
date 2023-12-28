
def sub(a,b):
    return a-b


#Decorator
def smartSub(fptr):
    def inner(a,b):
        if(a<b):
            a,b=b,a
        return fptr(a,b)
    return inner

def main():

    sub1 = smartSub(sub)

    ret=sub1(101,91)
    print("Subtraction is ",ret)

    ret=sub1(91,101)
    print("Subtraction is ",ret)

if __name__=="__main__":
    main()    