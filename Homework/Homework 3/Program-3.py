# Generate 5 random numbers and get thier average

import random

user_input = int(input("Enter A Number : "))

random_numbers = [random.randint(1, user_input) for _ in range(5)]
print(f"Random Numbers : {random_numbers}")

average = sum(random_numbers) / len(random_numbers)
print(f"Average Of Random Numbers Is : {average}")
