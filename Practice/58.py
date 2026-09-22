numbers = [int(value) for value in input("Enter Numbers : ").split()]
unique_numbers = []

for number in numbers:
    if number not in unique_numbers:
        unique_numbers.append(number)

print(unique_numbers)
