# Programming Assignment 1

## Exercise 1: Write a Python program to print "Hello World"

```python
print("Hello World")
```

---

## Exercise 2: Write a program to take 2 values from user, sum them, print the result

```python
number1 = int(input("Enter Number 1 : "))
number2 = int(input("Enter Number 2 : "))
print(f"Sum Of {number1} And {number2} Is {number1 + number2}")
```

---

## Exercise 3: Demonstrate `id()`, `type()`, `sep`, `end`, bitwise operators (`|`, `&`, `^`, `<<`, `>>`)

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

---

## Exercise 4: Write a program for net amount payable on purchasing Electronic goods

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

---

## Exercise 5: Write a program to find the sum of all the elements in a list

```python
finalList = []
numOfElements = int(input("Enter The Number Of Elements In The List : "))

for i in range(numOfElements):
    element = int(input("Enter The Element : "))
    finalList.append(element)

print("The List Is : ", finalList)
print("The Sum Of Elements : ", sum(finalList))
```

---

## Exercise 6: Write a program to find the maximum and minimum element in a list

```python
finalList = []
numOfElements = int(input("Enter The Number Of Elements In The List : "))

for i in range(numOfElements):
    element = int(input("Enter The Element : "))
    finalList.append(element)

print("The List Is : ", finalList)
print("The Maximum Element : ", max(finalList))
print("The Minimum Element : ", min(finalList))
```

---

## Exercise 7: Write a program to print the number of a particular element in a list

```python
finalList = []
numOfElements = int(input("Enter The Number Of Elements In The List : "))
