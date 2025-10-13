# generate a random number and cehck weather it is a perfect square or not

import random


def perfect_square(num):
    if num < 0:
        return False

    root = int(num**0.5)
    return root * root == num


user_input = int(input("Enter A Number : "))
random_number = random.randint(1, user_input)

if perfect_square(random_number):
    print(f"{random_number} Is A Perfect Square")
else:
    print(f"{random_number} Is Not A Perfect Square")
