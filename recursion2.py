i=0

def display() : 
    global i
    i=i+1
    print("Inside Display ",i)
    display()


def main():
        display()

if __name__=="__main__":
    main()   