# Write a Python program to simulate a lottery draw that picks 6 unique random numbers between 1 and 50.

import random


def lottery_draw():
    return random.sample(range(1, 51), 6)


drawn_numbers = lottery_draw()
print("Lottery Drawn Numbers:", drawn_numbers)
