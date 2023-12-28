#Function accepts multiple parameters and returns multiple parameter (Only possible in python )

def marvellous(value1,value2):
    addition = value1 + value2
    subtraction = value1 - value2
    multiplication = value1 * value2

    return addition, subtraction, multiplication

def main():
#    ret1, ret2, ret3 = marvellous(50,21)
#    print("Addition is ",ret1)
#    print("Substration is ",ret2)
#    print("Multiplication is",ret3)

   ret= marvellous(50,21)
   print(type(ret))
   print("Addition is ",ret[0])
   print("Substration is ",ret[1])
   print("Multiplication is",ret[2])




if __name__=="__main__":
    main()    