# Calculate a factorial of a number using random

import random


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


user_input = int(input("Enter A Number : "))

num = random.randint(1, user_input)

print(f"Random Number : {num}")
print(f"Factorial Of {num} Is {factorial(num)}")
