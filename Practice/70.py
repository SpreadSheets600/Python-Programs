list_values = input("Enter List Values : ").split()
tuple_values = tuple(list_values)
tuple_input = tuple(input("Enter Tuple Values : ").split())
list_from_tuple = list(tuple_input)

print(f"Tuple : {tuple_values}")
print(f"List : {list_from_tuple}")
