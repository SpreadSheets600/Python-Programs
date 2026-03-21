numbers = [int(value) for value in input("Enter Numbers : ").split()]

for index in range(len(numbers)):
    for inner_index in range(index + 1, len(numbers)):
        if numbers[index] > numbers[inner_index]:
            numbers[index], numbers[inner_index] = numbers[inner_index], numbers[index]

print(numbers)
