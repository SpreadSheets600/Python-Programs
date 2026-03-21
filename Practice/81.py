def largest_element(items):
    largest = items[0]

    for item in items:
        if item > largest:
            largest = item

    return largest


numbers = [int(value) for value in input("Enter Numbers : ").split()]
print(f"Largest Element : {largest_element(numbers)}")
