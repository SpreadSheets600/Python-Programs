num = int(input("Enter A Number : "))
factorial = 1

for number in range(1, num + 1):
    factorial *= number

print(f"Factorial : {factorial}")
