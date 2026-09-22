def total_sum(*numbers):
    total = 0

    for number in numbers:
        total += number

    return total


values = [int(value) for value in input("Enter Numbers : ").split()]
print(f"Sum : {total_sum(*values)}")
