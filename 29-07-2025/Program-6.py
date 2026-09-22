# Write A Program To Sort A List

finalList = []
numOfElements = int(input("Enter The Number Of Elements In The List : "))

for i in range(numOfElements):
    element = int(input("Enter The Element : "))
    finalList.append(element)

print("The List Is : ", finalList)

finalList.sort()
print("The List After Sorting : ", finalList)
