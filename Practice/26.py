num = int(input("Enter A Number : "))
count = 0

if num == 0:
    count = 1
else:
    num = abs(num)
    while num > 0:
        count += 1
        num //= 10

print(f"Digit Count : {count}")
