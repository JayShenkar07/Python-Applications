
def sub(a,b):
    # if (a<b):   #NO USE OF DECORATOR as we modified our function 
    #     a,b=b,a   #swap
    return a-b

def main():
    ret=sub(101,91)
    print("Subtraction is ",ret)

    ret=sub(91,101)
    print("Subtraction is ",ret)

if __name__=="__main__":
    main()    