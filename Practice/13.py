num_1 = float(input("Enter Number 1 : "))
num_2 = float(input("Enter Number 2 : "))
num_3 = float(input("Enter Number 3 : "))

greatest = num_1

if num_2 > greatest:
    greatest = num_2

if num_3 > greatest:
    greatest = num_3

print(f"Greatest Number : {greatest}")
