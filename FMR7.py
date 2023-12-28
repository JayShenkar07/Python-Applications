# from functools import reduce
import MarvellousFMR

#Other methods to import the module
# from MarvellousFMR import filterX
# from MarvellousFMR import mapX
# from MarvellousFMR import reduceX


#And then while calling the above functions we need not to write MarvellousFMR.function_name  ....we directly call the function by its name

#also we can import by 




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
    output=list(MarvellousFMR.filterX(checkEven, data))
    print("Output after Filter ", output)
    moutput=list(MarvellousFMR.mapX(inc, output))
    print("Output after Map ", moutput)

    result=MarvellousFMR.reduceX(add,moutput)
    print("Output after Reduce ", result)



if __name__=="__main__":
    main()


    #Filter Map Reduce is an important concept for interviews: 