#demonstration of default arguments: 
def display(name,age, marks = 22):  
    print("Name : ",name)
    print("Age : ",age)
    print("Marks : ",marks)        
    print(" ")

def main():
      display("Jay",20, 98)
      display("Virat", 97)
if __name__=="__main__":
    main()    