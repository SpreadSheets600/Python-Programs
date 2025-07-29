# Write A Program To Print The Number Of Particular Element In A List

finalList = []
numOfElements = int(input("Enter The Number Of Elements In The List : "))

for i in range(numOfElements):
    element = int(input("Enter The Element : "))
    finalList.append(element)

print("The List Is : ", finalList)

elementToCount = int(input("Enter The Element To Count : "))
print("The Count Of Element", elementToCount, "In The List Is : ", finalList.count(elementToCount))
