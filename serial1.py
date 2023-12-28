def fun(no):
    sum=0
    for i in range(100000):
        sum=sum+(no*no)
    return sum

def main():
    print("Demonstration of serial execution using single core")

    result = []
    for no in range(10000):      #highly heavy operation ...does  iteration 10000 time in this loop which will call function which runs 100000
        result.append(fun(no))
    

if __name__=="__main__":
    main()    