#set datatype demo

def main():
    s1={11,"Hellloooo",252.66,True}
    print(s1)

    for i in s1:                    #this is the only way to iterate the set
        print(i)
    
    # for i in range(len(s1)):  
    #     print(s1[0])              #indexing not possible

    s2={11,25,1,1,111,12,2,122,52,22,2,12,1}
    print(s2)                       #Stores only unique values

    #Mutablity
    #here in set we cant access any particular element as it is unordered and unindexed 
    #so ****DATA IS NOT MUTABLE**** in sets
    #But SET is Mutable
    print("  ")
    print(s1)
    s1.add(100)
    print(s1)
    s1.remove(True)    #We need to give the Value as Indexing is not possible in set
    print(s1)
    s1.discard(100)

    

if __name__=="__main__":
    main()