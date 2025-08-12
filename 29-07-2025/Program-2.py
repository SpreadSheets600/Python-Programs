# Write A Program To Find The Maximum And Minimum Element In A List

finalList = []
numOfElements = int(input("Enter The Number Of Elements In The List : "))

for i in range(numOfElements):
    element = int(input("Enter The Element : "))
    finalList.append(element)

print("The List Is : ", finalList)
print("The Maximum Element : ", max(finalList))
