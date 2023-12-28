import multiprocessing
import os

def task1(value):
    print("Executing the first task...")
    print("PID of task1 is : ",os.getpid()) 
    print("PID of parent process of task 1 is : ",os.getppid())
  

def task2(value):
    print("Executing the second task...")
    print("PID of task2 is : ",os.getpid())  
    print("PID of parent process of task 2 is : ",os.getppid())
 

def main():
    print("Demonstration of Multitasking with Multiprocessing : Starting with parallel execution")
    print("PID of running process is : ",os.getpid())
    no=5
    p1= multiprocessing.Process(target= task1, args=(no,))

    p2= multiprocessing.Process(target= task2, args=(no,))

    p1.start()
    p2.start()
    p1.join()
    p2.join()


if __name__=="__main__":
    main()    