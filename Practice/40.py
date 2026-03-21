limit = int(input("Enter A Number : "))
count = 0

for number in range(1, limit + 1):
    if number % 3 == 0 and number % 5 != 0:
        count += 1

print(f"Count : {count}")
