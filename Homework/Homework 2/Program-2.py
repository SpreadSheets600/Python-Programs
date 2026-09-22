# Generating a nested list using user input

nested_list = []
num_of_sublists = int(input("Enter The Number Of Sublist : "))

for i in range(num_of_sublists):
    sublist = []

    num_of_elements = int(input(f"Enter The Number Of Elements In Sublist {i + 1} : "))

    for j in range(num_of_elements):
        element = int(input(f"Enter Element {j + 1} For Sublist {i + 1} : "))
        sublist.append(element)

    nested_list.append(sublist)

print("Nested List : ", nested_list)
