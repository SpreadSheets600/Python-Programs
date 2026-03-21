numbers = [int(value) for value in input("Enter Numbers : ").split()]

if numbers:
    numbers = [numbers[-1]] + numbers[:-1]

print(numbers)
