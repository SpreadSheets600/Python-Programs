list_1 = [int(value) for value in input("Enter First List : ").split()]
list_2 = [int(value) for value in input("Enter Second List : ").split()]
common_elements = []

for number in list_1:
    if number in list_2 and number not in common_elements:
        common_elements.append(number)

print(common_elements)
