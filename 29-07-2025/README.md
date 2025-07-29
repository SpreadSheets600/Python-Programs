# Programming Exercises - July 29, 2025

## Exercise 1 : Write A Program To Find The Sum Of All The Elements In A List

```python
finalList = []
numOfElements = int(input("Enter The Number Of Elements In The List : "))

for i in range(numOfElements):
    element = int(input("Enter The Element : "))
    finalList.append(element)

print("The List Is : ", finalList)
print("The Sum Of Elements : ", sum(finalList))
```

## Exercise 2 : Write A Program To Find The Maximum And Minimum Element In A List

```python
finalList = []
numOfElements = int(input("Enter The Number Of Elements In The List : "))

for i in range(numOfElements):
    element = int(input("Enter The Element : "))
    finalList.append(element)

print("The List Is : ", finalList)
print("The Maximum Element : ", max(finalList))
print("The Minimum Element : ", min(finalList))
```

## Write A Program To Print The Number Of Particular Element In A List

```python
finalList = []
numOfElements = int(input("Enter The Number Of Elements In The List : "))

for i in range(numOfElements):
    element = int(input("Enter The Element : "))
    finalList.append(element)

print("The List Is : ", finalList)

elementToCount = int(input("Enter The Element To Count : "))
print("The Count Of Element", elementToCount, "In The List Is : ", finalList.count(elementToCount))
```

## Write A Program To Remove Duplicates From A List

```python
finalList = []
numOfElements = int(input("Enter The Number Of Elements In The List : "))

for i in range(numOfElements):
    element = int(input("Enter The Element : "))
    finalList.append(element)

print("The List Is : ", finalList)
finalList = list(set(finalList))

print("The List After Removing Duplicates : ", finalList)
```

## Write A Program To Reverse A List

```python
finalList = []
numOfElements = int(input("Enter The Number Of Elements In The List : "))

for i in range(numOfElements):
    element = int(input("Enter The Element : "))
    finalList.append(element)

print("The List Is : ", finalList)

finalList.reverse()
print("The List After Reversing : ", finalList)
```

## Write A Program To Sort A List

```python
finalList = []
numOfElements = int(input("Enter The Number Of Elements In The List : "))

for i in range(numOfElements):
    element = int(input("Enter The Element : "))
    finalList.append(element)

print("The List Is : ", finalList)

finalList.sort()
print("The List After Sorting : ", finalList)
```

## Write A Program To Merge Two Lists

```python
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
```
