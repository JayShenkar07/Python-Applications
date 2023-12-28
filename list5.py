#Testing Properties of Lists

def main():
    List1=[10,"Hello",515.2,True]   #List is Heterogeneous
    print(List1)                    #List is Ordered
    print(List1[0])                 #List is Indexed

    List2=[11,52,62,52,66,41,26,30] #Duplication Allowed
    print(List2)
    List2[2]=100                    #List is Mutable (Data Mutabilitiy)
    print(List2)            
    #Mutable comes with 2 things 
    #First- Data Is Mutable     We checked this on Line10
    #Second- List Is Mutable
    List2.append(99)
    print(List2)                    #List is Mutable (List Mutability)
    List2.remove(52)
    #Since we tried to remove an duplicate element ..the first val we get is removed
    print(List2)
    List2.pop() #Removes last element
    print(List2)




if __name__=="__main__":
    main()