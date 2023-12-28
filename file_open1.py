import os

def main():
    print("Enter the name of ile that you want to open for reading purporse:  ")

    file_name=input()
    if os.path.exists(file_name):
        fobj=open(file_name, "r")

        if fobj:
            print("File is sucessfully opened :  ")
            fobj.close()

    else:
        print("There is no such file : ")        


if __name__=="__main__":
    main()    