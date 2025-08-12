# Write A Program To Reverse A List

finalList = []
numOfElements = int(input("Enter The Number Of Elements In The List : "))

for i in range(numOfElements):
    element = int(input("Enter The Element : "))
    finalList.append(element)

print("The List Is : ", finalList)

finalList.reverse()
print("The List After Reversing : ", finalList)
