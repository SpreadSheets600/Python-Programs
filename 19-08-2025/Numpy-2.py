import numpy as np

# Reshaping A Numpy Array
myArray = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print("Original Array:", myArray)

reshapedArray = myArray.reshape(2, 5)
print("Reshaped Array (2 Rows, 5 Columns):", reshapedArray)

# Operations On Numpy Arrays
print("Sum of myArray:", np.sum(myArray))  # Sum Of All Elements
print("Mean of myArray:", np.mean(myArray))  # Mean Of All Elements
print(
    "Standard Deviation of myArray:", np.std(myArray)
)  # Standard Deviation Of All Elements

# Mathematical Operations
array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])

print("Element-wise Addition:", array1 + array2)  # Element-wise Addition
print("Element-wise Subtraction:", array1 - array2)  # Element-wise Subtraction
print("Element-wise Multiplication:", array1 * array2)  # Element-wise Multiplication
print("Element-wise Division:", array1 / array2)  # Element-wise Division


print("Dot Product of array1 and array2:", np.dot(array1, array2))  # Dot Product
print("Cross Product of array1 and array2:", np.cross(array1, array2))  # Cross Product

# Coloumn Wise - Row Wise Operations
matrix = np.array([[1, 2, 3], [4, 5, 6]])
print("Original Matrix:\n", matrix)

print("Sum Of Each Column:", np.sum(matrix, axis=0))  # Sum Of Each Column
print("Sum Of Each Row:", np.sum(matrix, axis=1))  # Sum Of Each Row

# Creating Special Matrices
identity_matrix = np.identity(3)  # Identity Matrix - 3 Rows, 3 Columns
print("Identity Matrix:\n", identity_matrix)

zero_matrix = np.zeros((2, 3))  # Zero Matrix - 2 Rows, 3 Columns
print("Zero Matrix:\n", zero_matrix)
