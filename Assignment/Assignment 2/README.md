# Programming Assignment : Assignment 2

---

## Program 1 : From a list, generate a new list of squares of even numbers only

```python
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

squaresOfEven = [ x ** 2 for x in lst if x % 2 == 0 ]
print("Squared List : ", squaresOfEven)
```

OUTPUT :

```bash
Squared List :  [4, 16, 36, 64, 100]

```

---

## Problem 2 : Find the Sum and Average of List Elements

```python
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

sumOfList = sum(lst)
averageOfList = sumOfList / len(lst)

print("Sum of List Elements : ", sumOfList)
print("Average of List Elements : ", averageOfList)
```

OUTPUT :

```bash
Sum of List Elements :  55
Average of List Elements :  5.5

```

---

## Program 3 : Write a program to convert list of strings to integers

```python
lst = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]

intList = [int(x) for x in lst]
print("Converted List of Integers : ", intList)
```

OUTPUT :

```bash
Converted List of Integers :  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

```

---

## Program 4 : Take a tuple and unpack its elements into variables and print them

```python
tup = (1, 2, 3, 4, 5)
a, b, c, d, e = tup

print("Unpacked Variables : ")
print("a =", a)
print("b =", b)
print("c =", c)
print("d =", d)
print("e =", e)

# Other Method ~
print("Upack Operator : ", *tup)
```

OUTPUT :

```bash
Unpacked Variables :
a = 1
b = 2
c = 3
d = 4
e = 5
Upack Operator :  1 2 3 4 5

```

---

## Program 5 : Find the tuple from a list of tuples that has the maximum sum of elements

```python
lst_of_tuples = [(1, 2, 3), (4, 5), (6, 7, 8, 9), (10,)]

max_tuple = max(lst_of_tuples, key=lambda x: sum(x))

print("Tuple with Maximum Sum of Elements : ", max_tuple)
print("Sum of Elements in this Tuple : ", sum(max_tuple))
```

OUTPUT :

```bash
Tuple with Maximum Sum of Elements :  (6, 7, 8, 9)
Sum of Elements in this Tuple :  30

```

---

## Program 6 : Tuples are immutable. Replace an element by converting the tuple to a list and back

```python
tup = (1, 2, 3, 4, 5)
lst = list(tup)

lst[2] = 99
tup = tuple(lst)

print("Modified Tuple : ", tup)
```

OUTPUT :

```bash
Modified Tuple :  (1, 2, 99, 4, 5)

```

---
