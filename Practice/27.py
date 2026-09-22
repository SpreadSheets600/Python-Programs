num = int(input("Enter A Number : "))
total = 0

for digit in str(abs(num)):
    total += int(digit)

print(f"Sum Of Digits : {total}")
