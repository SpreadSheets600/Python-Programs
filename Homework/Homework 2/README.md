# Programming Assignment : Homework 2

---

## Program 1 : Square each number in a nested list

```python
nested_list = [[1, 2], [3, 4], [5, 6]]
squared_list = []

for sublist in nested_list:
    squared_sublist = [num ** 2 for num in sublist]
    squared_list.append(squared_sublist)


print("Squared Nested List : ", squared_list)
```

**Sample Output:**

```bash
Squared Nested List :  [[1, 4], [9, 16], [25, 36]]
```

---

## Program 2 : Generating a nested list using user input

```python
nested_list = []
num_of_sublists = int(input("Enter The Number Of Sublist : "))

for i in range(num_of_sublists):
    sublist = []

    num_of_elements = int(input(f"Enter The Number Of Elements In Sublist {i + 1} : "))

    for j in range(num_of_elements):
        element = int(input(f"Enter Element {j + 1} For Sublist {i + 1} : "))
        sublist.append(element)

    nested_list.append(sublist)

print("Nested List : ", nested_list)
```

**Sample Output:**

```bash
Enter The Number Of Sublist : 2
Enter The Number Of Elements In Sublist 1 : 3
Enter Element 1 For Sublist 1 : 1
Enter Element 2 For Sublist 1 : 2
Enter Element 3 For Sublist 1 : 3
Enter The Number Of Elements In Sublist 2 : 2
Enter Element 1 For Sublist 2 : 4
Enter Element 2 For Sublist 2 : 5
Nested List :  [[1, 2, 3], [4, 5]]
```

---

## Program 3 : Create a tuple using user input

```python
lst = []

num_of_elements = int(input("Enter The Number Of Elements In The Tuple: "))

for i in range(num_of_elements):
    element = input(f"Enter Element {i + 1}: ")
    lst.append(element)

tuple_from_input = tuple(lst)

print("Tuple Created From User Input: ", tuple_from_input)
```

**Sample Output:**

```bash
Enter The Number Of Elements In The Tuple: 3
Enter Element 1: 1
Enter Element 2: 2
Enter Element 3: 3
Tuple Created From User Input:  (1, 2, 3)
```

---

## Program 4 : Find length of any tuple

```python
tup = (1, 2, 3, 4, 5)
length_of_tuple = len(tup)

print("Length of Tuple: ", length_of_tuple)
```

**Sample Output:**

```bash
Length of Tuple:  5
```

---

## Program 5 : Count occurances of an element

```python
tup = (1, 2, 3, 4, 5, 3, 2, 1)

element_to_count = 3
count_of_element = tup.count(element_to_count)

print(f"The Element {element_to_count} Occurs : ", count_of_element)
```

**Sample Output:**

```bash
The Element 3 Occurs :  2
```

---

## Program 6 : Concatinate two tuples

```python
tup1 = (1, 2, 3)
tup2 = (4, 5, 6)

concatenated_tuple = list(tup1) + list(tup2)

print("Concatenated Tuple : ", tuple(concatenated_tuple))
```

**Sample Output:**

```bash
Concatenated Tuple :  (1, 2, 3, 4, 5, 6)
```

---

## Program 7 : Convert list to tuple

```python
lst = [1, 2, 3, 4, 5]
tup = tuple(lst)

print("Converted Tuple : ", tup)
```

**Sample Output:**

```bash
Converted Tuple :  (1, 2, 3, 4, 5)
```

---
