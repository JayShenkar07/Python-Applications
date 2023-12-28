#demonstration of variable number of arguments: 
def display(*value):
    for i in range(len(value)):
        print(value[i])        
    print(" ")
    
def main():
      display(20,30)
      display(10,50,39,25,12,2,5)
if __name__=="__main__":
    main()    