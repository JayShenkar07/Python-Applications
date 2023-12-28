import os

def main():
    print("Enter the name of the file that you want to delete:  ")
    
    file_name=input()
    if os.path.exists(file_name):
        os.remove(file_name)

    else:
        print("There is no such file to delete: ")

if __name__=="__main__":
    main()    