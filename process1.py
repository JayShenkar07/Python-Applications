import os
def main():
    print("PID of the current process is : ", os.getpid())

    print("PID of the parent process is : ", os.getppid())   #This is the process id of the parent (It gives us the pid of cmd)

if __name__=="__main__":
    main()    