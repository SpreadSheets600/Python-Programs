count = int(input("Enter Number Of Items : "))
data = {}

for index in range(1, count + 1):
    key = input(f"Enter Key {index} : ")
    value = input(f"Enter Value {index} : ")
    data[key] = value

print("Keys")
for key in data.keys():
    print(key)

print("Values")
for value in data.values():
    print(value)

print("Key Value Pairs")
for key, value in data.items():
    print(key, value)
