class Arithmatic:
    def __init__(self, A, B):
        print("Inside Constructor")
        self.no1 = A
        self.no2 = B
        
    def addition(self):
        ans = self.no1 + self.no2
        return ans
    
    def subtraction(self):
        ans = self.no1 - self.no2
        return ans

def main():
    num1 = int(input("Enter 1st no: "))
    num2 = int(input("Enter 2nd no: "))

    obj1 = Arithmatic(num1, num2)

    ret = obj1.addition()
    print("Addition:", ret)

    ret = obj1.subtraction()
    print("Subtraction:", ret)

if __name__ == "__main__":
    main()


