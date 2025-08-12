# Program 1 : From a list, generate a new list of squares of even numbers only.

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

squaresOfEven = [ x ** 2 for x in lst if x % 2 == 0 ]
print("Squared List : ", squaresOfEven)
