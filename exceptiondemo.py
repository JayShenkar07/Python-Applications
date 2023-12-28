def main():
    no1=int(input("Enter the 1st no: "))
    try: 
        no2=int(input("Enter the 2nd no:  "))
        ans=0
    # code written inside the try block is run under the observation of the PVM 
    # So, PVM critically monitors the try block 
        ans=no1/no2

    except ZeroDivisionError as zobj:
        print("Division by zero is not allowed ",zobj)
        return
    
    except ValueError as zobj1:
        print('Value  Error Excpetion !!',zobj1)
        return

    except Exception as zobj2:
        print("Exception Occurred ",zobj2)  
        return #Generic Exception 

# PVM takes care to run the finally block unconditionally 

    finally:
        print("Finally Block __This runs everytime no matter exception is occured or not: ")
    print(ans)

if __name__=="__main__":
    main()