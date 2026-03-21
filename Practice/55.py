numbers = []

for index in range(1, 11):
    numbers.append(int(input(f"Enter Number {index} : ")))

print(f"Largest : {max(numbers)}")
print(f"Smallest : {min(numbers)}")
