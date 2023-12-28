import os
def main():
    print("Enter the name of file that you want to open for reading purporse:  ")

    file_name=input()
    if os.path.exists(file_name):
        fobj=open(file_name, "r")

        if fobj:
            print("File is sucessfully opened :  ")
            line1=fobj.readline()
            line2=fobj.readline()
            line3=fobj.readline()

            print("Line 1 : ",line1)
            print("Line 2 : ",line2)
            print("Line 3 : ",line3)

            print("Data from the file:  " )
            for line in fobj:
                print(line)

            fobj.close()
    else:
        print("There is no such file : ")        


if __name__=="__main__":
    main()    