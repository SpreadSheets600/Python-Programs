# Generate random number and check weather it is prime or not

import random


def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False

    return True


user_input = int(input("Enter A Number : "))

random_number = random.randint(1, user_input)

if is_prime(random_number):
    print(f"{random_number} Is A Prime Number")
else:
    print(f"{random_number} Is Not A Prime Number")
