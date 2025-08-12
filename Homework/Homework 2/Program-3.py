# Create a tuple using user input

lst = []

num_of_elements = int(input("Enter The Number Of Elements In The Tuple: "))

for i in range(num_of_elements):
    element = input(f"Enter Element {i + 1}: ")
    lst.append(element)

tuple_from_input = tuple(lst)

print("Tuple Created From User Input: ", tuple_from_input)
