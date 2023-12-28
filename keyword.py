#demonstration of keyword arguments: 
def display(name,age,marks):
    print("Name : ",name)
    print("Age : ",age)
    print("Marks : ",marks)        
    print(" ")
def main():
    display(name="Jay",age=20,marks=98)
    display(marks=97, age=21, name="Virat")
if __name__=="__main__":
    main()    