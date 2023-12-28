import os
import threading

def task1():
    print("PID of task1 is : ",os.getpid())
    print("Thread ID of first thread is ", threading.get_ident())

def task2():
    print("PID of task2 is : ",os.getpid())
    print("Thread ID of second thread is ", threading.get_ident())


def main():
     print("PID of parent process is : ",os.getpid())
     no=5
     t1=threading.Thread(target= task1)
     t2=threading.Thread(target= task2)

     t1.start()
     t2.start()

     t1.join()
     t2.join()



if __name__=="__main__":
    main()