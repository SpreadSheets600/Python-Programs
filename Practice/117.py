def unique_elements(items):
    result = []

    for item in items:
        if item not in result:
            result.append(item)

    return result


items = input("Enter Items : ").split()
print(unique_elements(items))
