#Function accepts parameters and call other function

# def add(a,b):
#     return a+b

add = lambda a,b : a+b

sub = lambda a,b : a-b

# def sub(a,b):
#     return a-b

def marvellous(val1,val2):
  ans1= add(val1, val2)
  ans2=sub(val1,val2)
  return ans1, ans2


def main():
    arr= marvellous(822,3615)
    print("Addition: ",arr[0])
    print("Subtraction: ",arr[1])
if __name__=="__main__":
    main()    


