numbers = [int(value) for value in input("Enter Numbers : ").split()]
frequency = {}

for number in numbers:
    frequency[number] = frequency.get(number, 0) + 1

print(frequency)
