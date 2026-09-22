# Program 5 : Find the tuple from a list of tuples that has the maximum sum of elements.

lst_of_tuples = [(1, 2, 3), (4, 5), (6, 7, 8, 9), (10,)]

max_tuple = max(lst_of_tuples, key=lambda x: sum(x))

print("Tuple with Maximum Sum of Elements : ", max_tuple)
print("Sum of Elements in this Tuple : ", sum(max_tuple))

