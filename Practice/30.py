num = int(input("Enter A Number : "))
digits = str(abs(num))
power = len(digits)
total = 0

for digit in digits:
    total += int(digit) ** power

if total == abs(num):
    print("Armstrong Number")
else:
    print("Not Armstrong Number")
