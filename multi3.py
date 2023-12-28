import multiprocessing
import os

def task1(value):
    print("Executing the first task...")
    for i in range(value):
        print("Task1 ",i)
  

def task2(value):
    print("Executing the second task...")
    for i in range(value):
        print("Task2 ",i)
    

 

def main():
    print("Demonstration of Multitasking with Multiprocessing : Starting with parallel execution")

    no1=500
    no2=800
    p1= multiprocessing.Process(target= task1, args=(no1,))

    p2= multiprocessing.Process(target= task2, args=(no2,))

    p1.start()
    p2.start()
    p1.join()
    p2.join()


print("Context switching can be seen clearly here! ")
#OS assigns quantum time for each process for execution of each process after which it switches to other and comes back again... OS Rizzzz boisss

if __name__=="__main__":
    main()    