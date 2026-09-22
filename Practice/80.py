def sum_of_digits(number):
    total = 0

    for digit in str(abs(number)):
        total += int(digit)

    return total


num = int(input("Enter A Number : "))
print(f"Sum Of Digits : {sum_of_digits(num)}")
