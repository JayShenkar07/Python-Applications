#Function accepts parameters and call other function

def add(a,b):    #0x000001995B364E50    (reference)
                                        #text data stack 
                                        # This hashcode refers to text section (binary converted)   
    return a+b


def marvellous(fptr1):
    print(type(fptr1))
    print(fptr1)       #<function add at 0x000001995B364E50> 
    ans=fptr1(11,7)    #ans = 0x000001995B364E50(11,7)
    print("Addition is ",ans)


def main():
    marvellous(add)   #marvellous(0x000001995B364E50)
   
if __name__=="__main__":
    main()    


