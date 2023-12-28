import os.path

def main():
    print("Enter the name of the file that you want to create:  ")
    
    file_name=input()
    if os.path.exists(file_name):
        print("Unable to create the file as file by this name already exists: ")

    else:
        fobj=open(file_name, "x")  
    

if __name__=="__main__":
    main()    