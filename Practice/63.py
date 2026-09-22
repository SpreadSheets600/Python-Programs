numbers = [int(value) for value in input("Enter Numbers : ").split()]
positive_numbers = []
negative_numbers = []

for number in numbers:
    if number >= 0:
        positive_numbers.append(number)
    else:
        negative_numbers.append(number)

print(f"Positive Numbers : {positive_numbers}")
print(f"Negative Numbers : {negative_numbers}")
