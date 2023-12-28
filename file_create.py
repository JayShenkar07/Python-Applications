def main():
    print("Enter the name of the file that you want to create:  ")
    
    file_name=input()

    fobj=open(file_name, "x")  #Open function is used to create and open the file (Unlike in C we have open() and create()  such methods)
    

if __name__=="__main__":
    main()    