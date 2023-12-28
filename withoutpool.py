def square(no):
    return no * no

def main():
    arr=[10,20,30,40]
    Result=[]

    for value in arr:
        ans= square(value)
        Result.append(ans)

    print(Result)



if __name__=="__main__":
    main()

