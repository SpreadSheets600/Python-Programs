count_1 = int(input("Enter Number Of Items In First Dictionary : "))
dict_1 = {}

for index in range(1, count_1 + 1):
    key = input(f"Enter First Dictionary Key {index} : ")
    value = input(f"Enter First Dictionary Value {index} : ")
    dict_1[key] = value

count_2 = int(input("Enter Number Of Items In Second Dictionary : "))
dict_2 = {}

for index in range(1, count_2 + 1):
    key = input(f"Enter Second Dictionary Key {index} : ")
    value = input(f"Enter Second Dictionary Value {index} : ")
    dict_2[key] = value

merged = dict_1.copy()
merged.update(dict_2)

print(merged)
