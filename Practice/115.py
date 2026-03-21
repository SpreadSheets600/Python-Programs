numbers = [int(value) for value in input("Enter Numbers : ").split()]
target = int(input("Enter Number To Search : "))

if target in numbers:
    print(f"Position : {numbers.index(target) + 1}")
else:
    print("Element Not Found")
