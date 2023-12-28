import multiprocessing


def square(no):
    return no * no

def main():
    arr=[10,20,30,40]
    Result=[]

#Will request for the available cores to perform certain tasks 
    p=multiprocessing.Pool()

#Assigning tasks to the cores available 
    Result = p.map(square, arr)
    p.close()
    p.join()  #Just like wait() sys call in unix systems
 
    print(Result)
  



if __name__=="__main__":
    main()

