# Importing Numpy And Making It Available As 'np'
# This Is A Good Practice To Follow And Maintain Consistency In Code
# Anything Can Be Put In Place Of 'np' But 'np' Is The Standard Alias For Numpy

import numpy as np

myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Original List :", myList)
print("Type of myList :", type(myList))

# Converting List To Numpy Array

myArray = np.array(myList)
print("Converted Numpy Array :", myArray)
print("Type of myArray :", type(myArray))

# Parameters Of Numpy Array
print("Shape Of myArray :", myArray.shape)  # Shape Of The Array

print("Length Of myArray :", len(myArray))  # Length Of The Array
print("Data Type Of myArray :", myArray.dtype)  # Data Type Of The Array Elements

print("Size Of myArray :", myArray.size)  # Total Number Of Elements In The Array
print("N Dimensions Of myArray :", myArray.ndim)  # Number Of Dimensions Of The Array

print(
    "Item Size Of myArray :", myArray.itemsize
)  # Size In Bytes Of Each Element In The Array

print("Memory Layout Of myArray :", myArray.flags)  # Memory Layout Information
