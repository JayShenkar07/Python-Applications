i=1

def display(no) :
    global i 
    if (i<=no):
        print(i)
        i=i+1
        display(no)

def main():
        display(5)

if __name__=="__main__":
    main()   