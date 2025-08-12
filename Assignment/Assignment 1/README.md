# Programming Assignment 1

## Program 1: Write a Python program to print "Hello World"

```python
print("Hello World")
```

### OUTPUT

```bash
Hello World
```

## Program 2: Write a program to take 2 values from user, sum them, print the result

```python
number1 = int(input("Enter Number 1 : "))
number2 = int(input("Enter Number 2 : "))
print(f"Sum Of {number1} And {number2} Is {number1 + number2}")
```

### OUTPUT

```bash
Enter Number 1 : 5
Enter Number 2 : 5
Sum Of 5 And 5 Is 10
```

## Program 3: Demonstrate `id()`, `type()`, `sep`, `end`, bitwise operators (`|`, `&`, `^`, `<<`, `>>`)

```python
# User Input
a = int(input("Enter A Number : "))
b = float(input("Enter A Float :"))
c = str(input("Enter A String : "))

print("ID Of a :", id(a), "Type Of a :", type(a))
print("ID Of b :", id(b), "Type Of b :", type(b))
print("ID Of c :", id(c), "Type Of c :", type(c))

# Sep And End Parameters
print("Python", "is", "fun", sep="-", end="!\n")

# Bitwise Operators
x = 5  # 0b0101
y = 3  # 0b0011

print("x | y =", x | y)  # Bitwise OR
print("x & y =", x & y)  # Bitwise AND
print("x ^ y =", x ^ y)  # Bitwise XOR

print("x << 1 =", x << 1)  # Left shift
print("x >> 1 =", x >> 1)  # Right shift
```

### OUTPUT

```bash
Enter A Number : 2
Enter A Float :3.33
Enter A String : SOHAM
ID Of a : 139892576275760 Type Of a : <class 'int'>
ID Of b : 139892333066416 Type Of b : <class 'float'>
ID Of c : 139892332575600 Type Of c : <class 'str'>
Python-is-fun!
x | y = 7
x & y = 1
x ^ y = 6
x << 1 = 10
x >> 1 = 2
```

## Program 4: Write a program for net amount payable on purchasing Electronic goods

- If Cost >= 50000: discount 15%
- If Cost between 30000 to 50000: discount 10%
- If Cost between 20000 to 30000: discount 5%

```python
cost = int(input("Enter The Cost Of Electronic Goods : "))

if cost >= 50000:
    discount = cost * 0.15
    print("The Discounted Price Is : ", cost - discount)
elif 30000 <= cost < 50000:
    discount = cost * 0.10
    print("The Discounted Price Is : ", cost - discount)
elif 20000 <= cost < 30000:
    discount = cost * 0.05
    print("The Discounted Price Is : ", cost - discount)
else:
    print("No Discount Available!")
```

### OUTPUT

```bash
Enter The Cost Of Electronic Goods : 32000
The Discounted Price Is :  28800.0
---
