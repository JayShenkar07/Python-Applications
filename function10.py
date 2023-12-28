#Function defines another function inside it (Inner Function) 

#Implementation of Abstraction in Python

def marvellous(val1,val2):    
    def add(a,b):                
        return a+b 

    return add(val1,val2)                                                                 

def main():
    ret=marvellous(11,21)
    print(ret)

if __name__=="__main__":
    main()    


