count = int(input("Enter Number Of Items : "))
data = {}

for index in range(1, count + 1):
    key = input(f"Enter Key {index} : ")
    value = input(f"Enter Value {index} : ")
    data[key] = value

inverted = {}

for key, value in data.items():
    inverted[value] = key

print(inverted)
