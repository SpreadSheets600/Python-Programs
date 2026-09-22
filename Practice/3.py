num_1 = float(input("Enter Number 1 : "))
num_2 = float(input("Enter Number 2 : "))

print(f"Sum : {num_1 + num_2}")
print(f"Difference : {num_1 - num_2}")
print(f"Product : {num_1 * num_2}")

if num_2 != 0:
    print(f"Quotient : {num_1 / num_2}")
    print(f"Remainder : {num_1 % num_2}")
else:
    print("Quotient : Not Possible")
    print("Remainder : Not Possible")
