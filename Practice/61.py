numbers = [int(value) for value in input("Enter Numbers : ").split()]
unique_numbers = []

for number in numbers:
    if number not in unique_numbers:
        unique_numbers.append(number)

if len(unique_numbers) < 2:
    print("Second Largest Element Does Not Exist")
else:
    unique_numbers.sort()
    print(f"Second Largest : {unique_numbers[-2]}")
