def factorial(number):
    result = 1

    for value in range(1, number + 1):
        result *= value

    return result


num = int(input("Enter A Number : "))
print(f"Factorial : {factorial(num)}")
