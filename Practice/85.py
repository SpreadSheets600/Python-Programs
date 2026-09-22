def factorial(number):
    if number <= 1:
        return 1
    return number * factorial(number - 1)


num = int(input("Enter A Number : "))
print(f"Factorial : {factorial(num)}")
