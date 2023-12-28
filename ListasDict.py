#Suppose a sceneario is made where we have to store item and its corresponding price with it but NOT using a Dictionary (which is the easiest way to do so)

itemList=["Nike","Addidas","Skechers","Puma","Woodland"]
priceList=[10000,12400,12000,9250,8100]

# for i in range(len(itemList)):
#     print("Item: ",itemList[i], "Price: ",priceList[i])

print("Item  Price")
for i in range(len(itemList)):
    print(itemList[i]," ",priceList[i])