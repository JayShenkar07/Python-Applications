#Function defines another function inside it (Inner Function) 

#Implementation of Abstraction in Python

def marvellous():     #wrapper function (broker)                                
    def add(a,b):           #inner function  (this function is abstracted out)         
        return a+b 

    return add                                                                 

def main():
    ret=marvellous()    
    ans=ret(11,21)
    print(ans)




if __name__=="__main__":
    main()    


