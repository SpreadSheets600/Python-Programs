# Programming Assignment : Assignment 5

---

## Program 1 : Choose a Random Element from a List

```python
# Choose a Random Element from a List.

import random

lst = [10, 20, 30, 40, 50]

print("Random Element : ", random.choice(lst))
```

**Sample Output:**

```bash
Random Element :  50
```

---

## Program 2 : Calculate Compound Interest

```python
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
```

**Sample Output:**

```bash
Compound Interest : 628.89
```

---

## Program 3 : Generate a 6-digit Random OTP

```python
# Generate a 6-digit random OTP.

import random

otp = random.randint(100000, 999999)
print("Your OTP is :", otp)
```

**Sample Output:**

```bash
Your OTP is : 981679
```

---

## Program 4 : Generate a Random Password

```python
# Write a Python program to generate a random password containing letters, digits, and special characters using the random module.

import random
import string


def generate_password(length):
    if length < 4:
        raise ValueError("Password length should be at least 4 characters.")

    all_characters = string.ascii_letters + string.digits + string.punctuation

    password = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice(string.punctuation),
    ]

    password += random.choices(all_characters, k=length - 4)

    random.shuffle(password)

    return "".join(password)


password_length = int(input("Enter the desired password length (minimum 4): "))
password = generate_password(password_length)
print("Generated Password:", password)
```

**Sample Output:**

```bash
Enter the desired password length (minimum 4): 8
Generated Password: GFpr%Z29
```

---

## Program 5 : Simulate a Lottery Draw

```python
# Write a Python program to simulate a lottery draw that picks 6 unique random numbers between 1 and 50.

import random


def lottery_draw():
    return random.sample(range(1, 51), 6)


drawn_numbers = lottery_draw()
print("Lottery Drawn Numbers:", drawn_numbers)
```

**Sample Output:**

```bash
Lottery Drawn Numbers: [12, 23, 34, 45, 6, 17]
```

---

## Program 6 : Check Armstrong Number

```python
# Write a Python program to check whether a given number is an Armstrong number or not.


def is_armstrong_number(num):
    num_str = str(num)
    num_digits = len(num_str)
    sum_of_powers = sum(int(digit) ** num_digits for digit in num_str)
    return sum_of_powers == num


number = int(input("Enter a number: "))

if is_armstrong_number(number):
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")
```

**Sample Output:**

```bash
Enter a number: 153
153 is an Armstrong number.
```

---
