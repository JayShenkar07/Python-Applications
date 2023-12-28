#Tuple Properties Demonstration: 
def main():
    tuple1=(10,"Jay",12.21,True)
    print(tuple1)
    #tuple1[0]=11
    #print(tuple1)                  tuple is not mutable
    # tuple1.append(256)
    # print(tuple1)
    print(tuple1[0])                #tuple is not indexed
    for i in tuple1:
        print(i)

    for i in range(len(tuple1)):
        print(tuple1[i],end=" ")    




if __name__=="__main__":
    main()