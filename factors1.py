No=int(input("Enter the number to check for its factors "))
print("The factors are ")
for i in range(1,No):
    if(No % i == 0):
        print(i)