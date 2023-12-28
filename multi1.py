import multiprocessing
import os

def task1():
    print("Executing the first task...")
    print("PID of task1 is : ",os.getpid())   

def task2():
    print("Executing the second task...")
    print("PID of task2 is : ",os.getpid())   

def main():
    print("Demonstration of Multitasking with Multiprocessing : Starting with serial execution")
    # print("PID of running process is : ",os.getpid())   

    task1()
    task2()


if __name__=="__main__":
    main()    