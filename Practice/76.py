count = int(input("Enter Number Of Items : "))
data = {}

for index in range(1, count + 1):
    key = input(f"Enter Key {index} : ")
    value = input(f"Enter Value {index} : ")
    data[key] = value

target_key = input("Enter Key To Search : ")

if target_key in data:
    print("Key Exists")
else:
    print("Key Does Not Exist")
