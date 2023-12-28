class demo:
    def __init__(self, value1, value2):                   #constructor
        print("Inside the init method")
        self.no1=value1
        self.no2=value2

    def display(self):
        print("Value of no1 is : ",self.no1)
        print("Value of no2 is : ",self.no2)
           
def main():
    print("_Demonstration of Object Orientation_")

obj1=demo(11,125)
obj2=demo(25,36)
obj1.display()
obj2.display()

if __name__=="__main__":
    main()