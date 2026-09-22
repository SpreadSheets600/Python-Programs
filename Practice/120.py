count = int(input("Enter Number Of Items : "))
total_bill = 0

for index in range(1, count + 1):
    item_name = input(f"Enter Item {index} Name : ")
    quantity = int(input(f"Enter Quantity Of {item_name} : "))
    price = float(input(f"Enter Price Of {item_name} : "))
    amount = quantity * price
    total_bill += amount
    print(f"{item_name} : {amount}")

print(f"Total Bill : {total_bill}")
