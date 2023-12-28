data=[11,21,51,101]

for i in range(len(data)):
    print(data[i], end=" ")

for i in range(0,len(data),1):
    print(data[i], end=" ")    
i=0
cnt=len(data)
while(cnt!=0):
    print(data[i])
    i=i+1
    cnt=cnt-1
