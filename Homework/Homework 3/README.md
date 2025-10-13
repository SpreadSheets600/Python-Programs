# Programming Assignment : Homework 3

---

## Program 1 : Generate random number and check if it is prime or not

```python
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
```

**Sample Output:**

```bash
Enter A Number : 6 Is Not A Prime Number
```

---

## Program 2 : Calculate factorial of a number using random

```python
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
```

**Sample Output:**

```bash
Enter A Number : Random Number : 3
Factorial Of 3 Is 6
```

---

## Program 3 : Generate 5 random numbers and get their average

```python
# Generate 5 random numbers and get thier average

import random

user_input = int(input("Enter A Number : "))

random_numbers = [random.randint(1, user_input) for _ in range(5)]
print(f"Random Numbers : {random_numbers}")

average = sum(random_numbers) / len(random_numbers)
print(f"Average Of Random Numbers Is : {average}")
```

**Sample Output:**

```bash
Enter A Number : Random Numbers : [8, 10, 2, 8, 9]
Average Of Random Numbers Is : 7.4
```

---

## Program 4 : Generate a random number and check if it is a perfect square or not

```python
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
```

**Sample Output:**

```bash
Enter A Number : 7 Is Not A Perfect Square
```

---

## Program 5 : Calculate tip for a bill with random tip percentage

```python
import random


def calculate_tip(bill, tip_percent):
    tip = bill * (tip_percent / 100)
    total = bill + tip
    return tip, total


def main():
    try:
        bill = float(input("Enter The Bill Amount : $"))

        tip_percent = random.randint(10, 20)
        tip, total = calculate_tip(bill, tip_percent)

        print(f"Tip : {tip:.2f}")
        print(f"Total : {total:.2f}")

    except ValueError:
        print("Please Enter Valid Amount")


if __name__ == "__main__":
    main()
```

**Sample Output:**

```bash
Enter The Bill Amount : $Tip : 20.00
Total : 120.00
```

---
