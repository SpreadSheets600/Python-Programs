numbers = [int(value) for value in input("Enter Numbers : ").split()]
even_count = 0
odd_count = 0

for number in numbers:
    if number % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print(f"Even Count : {even_count}")
print(f"Odd Count : {odd_count}")
