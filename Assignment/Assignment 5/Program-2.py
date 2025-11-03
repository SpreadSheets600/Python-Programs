# Write a Python program to calculate the compound interest for given principal, rate, and time using the math module.

import math


def compound_interest(principal, rate, time):
    ci = (principal * math.pow((1 + rate / 100), time)) - principal
    return ci


p = 1000
r = 5
t = 10

ci = compound_interest(p, r, t)
print(f"Compound Interest : {ci:.2f}")
