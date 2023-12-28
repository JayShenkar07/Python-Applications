#Task - Name of Function
#Elements - List of data elements
def filterX(task, elements):
    result=[]
    for no in elements:
        if(task(no) == True):
            result.append(no)
    return result


def mapX(task, elements):
    result = []
    for no in elements:
        res=task(no)
        result.append(res)
    return result    

def reduceX(task, elements):
    sum=0
    for no in elements:
        sum=task(sum , no)
    return sum
