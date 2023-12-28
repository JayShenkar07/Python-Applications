# from functools import reduce

checkEven = lambda no : no%2==0
inc=  lambda no : no+2
add = lambda a,b: a+b

#Task - Name of Function
#Elements - List of data elements
def filterX(task, elements):
    result=[]
    for no in elements:
        if(task(no) == True):
            result.append(no)
    return result


def mapX(task, elements):
    result = []
    for no in elements:
        res=task(no)
        result.append(res)
    return result    

def reduceX(task, elements):
    sum=0
    for no in elements:
        sum=task(sum , no)
    return sum


def main():
    data=[]
    print("Enter the number of elements: ")
    size=int(input())

    for i in range(0,size):
        item=int(input())
        data.append(item)

    print("Elements are accepted successfully! ")

    print()
    output=list(filterX(checkEven, data))
    print("Output after Filter ", output)
    moutput=list(mapX(inc, output))
    print("Output after Map ", moutput)

    result=reduceX(add,moutput)
    print("Output after Reduce ", result)



if __name__=="__main__":
    main()


    #Filter Map Reduce is an important concept for interviews: 