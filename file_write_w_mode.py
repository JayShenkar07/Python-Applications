import os

def main():
    print("Enter the name of file that you want to open for writing purporse:  ")
    file_name=input()

    if os.path.exists(file_name):
        fobj=open(file_name, "w")   # a append mode
                                     # w write mode (Deletes all the previous content of the file)
        if fobj:
            print("File is sucessfully opened in write mode:  ")
            print("Enter the data to write in the file:  ")
            Data=input()
            fobj.write(Data)
            fobj.close()

    else:
        print("There is no such file : ")        


if __name__=="__main__":
    main()    