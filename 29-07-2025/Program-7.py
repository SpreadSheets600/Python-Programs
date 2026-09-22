# Write A Program To Merge Two Lists

finalList1 = []
numOfElements1 = int(input("Enter The Number Of Elements In The First List : "))

for i in range(numOfElements1):
    element = int(input("Enter The Element : "))
    finalList1.append(element)

finalList2 = []
numOfElements2 = int(input("Enter The Number Of Elements In The Second List : "))

for i in range(numOfElements2):
    element = int(input("Enter The Element : "))
    finalList2.append(element)

print("The First List Is : ", finalList1)
print("The Second List Is : ", finalList2)

finalList1.extend(finalList2)
print("The Merged List Is : ", finalList1)
