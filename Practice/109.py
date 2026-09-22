def factorial(number):
    result = 1

    for value in range(1, number + 1):
        result *= value

    return result


num = int(input("Enter A Number : "))
original_num = num
total = 0

while num > 0:
    digit = num % 10
    total += factorial(digit)
    num //= 10

if total == original_num:
    print("Strong Number")
else:
    print("Not Strong Number")
