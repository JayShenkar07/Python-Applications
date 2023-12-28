import os

def main():
    print("Enter the name of file that you want to open for reading purporse:  ")

    file_name=input()
    if os.path.exists(file_name):
        fobj=open(file_name, "r")

        if fobj:
            print("File is sucessfully opened :  ")
            data=fobj.read(5)    #change: 5 bytes from the file
            print("Data from the file:    ",data)
            fobj.close()

    else:
        print("There is no such file : ")        


if __name__=="__main__":
    main()    