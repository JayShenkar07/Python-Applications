
#Simple iterative code inside funtion and the funtion's call
def fun(): #Callie
    for i in range (1,6):    
        print("Inside Funtion")
def gun():
    i=1
    while (i<=5):
        print(i)
        i=i+1

def main():
    fun()   #Caller
    gun()

if __name__=="__main__":
    main()   