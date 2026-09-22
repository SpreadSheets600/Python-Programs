file_name = "numbers_99.txt"
numbers = [int(value) for value in input("Enter Numbers : ").split()]

with open(file_name, "w") as file:
    for number in numbers:
        file.write(f"{number}\n")

total = 0

with open(file_name, "r") as file:
    for line in file:
        total += int(line.strip())

print(f"Sum : {total}")
