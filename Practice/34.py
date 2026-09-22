num_1 = int(input("Enter Number 1 : "))
num_2 = int(input("Enter Number 2 : "))

a = abs(num_1)
b = abs(num_2)

while b != 0:
    a, b = b, a % b

print(f"HCF : {a}")
