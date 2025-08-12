# Square each number in a nested list

nested_list = [[1, 2], [3, 4], [5, 6]]
squared_list = []

for sublist in nested_list:
    squared_sublist = [num ** 2 for num in sublist]
    squared_list.append(squared_sublist)


print("Squared Nested List : ", squared_list)

