# def displayfactors(num):
#     for i in range (1,num):
#         if(num%i==0):
#             print(i)

def displayfactors(num):
    i=1
    while(i<num):
        if(num%i==0):
            print(i)
            i=i+1

def main():
    num=int(input("Enter the number: "))
    displayfactors(num)

if __name__=="__main__":
    main()    