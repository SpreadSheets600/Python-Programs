# Programming Assignment: Homework 1 (List Operations)

---

## Program 1: Find the Sum of All Elements in a List

```python
lst = [1, 2, 3, 4, 5]
sum_of_elements = sum(lst)

print("The Sum of All Elements : ", sum_of_elements)
```

**Sample Output:**

```bash
The Sum of All Elements :  15
```

---

## Program 2: Find the Maximum Element in a List

```python
lst = [1, 2, 3, 4, 5]
max_element = max(lst)

print("The Maximum Element : ", max_element)
```

**Sample Output:**

```bash
The Maximum Element :  5
```

---

## Program 3: Count How Many Times an Element Occurs in a List

```python
lst = [1, 2, 3, 4, 5, 3, 2, 1]

element_to_count = 3
count_of_element = lst.count(element_to_count)

print(f"The Element {element_to_count} Occurs : ", count_of_element)
```

**Sample Output:**

```bash
The Element 3 Occurs :  2
```

---

## Program 4: Remove Duplicates from a List

```python
lst = [1, 2, 3, 4, 5, 3, 2, 1]
unique_elements = list(set(lst))

print("List After Removing Duplicates : ", unique_elements)
```

**Sample Output:**

```bash
List After Removing Duplicates :  [1, 2, 3, 4, 5]
```

---

## Program 5: Reverse a List

```python
lst = [1, 2, 3, 4, 5]
reversed_list = lst[::-1]

print("Reversed List : ", reversed_list)
```

**Sample Output:**

```bash
Reversed List :  [5, 4, 3, 2, 1]
```

---

## Program 6: Print List in Sorted Order

```python
lst = [5, 3, 1, 4, 2]
sorted_list = sorted(lst)

print("Sorted List : ", sorted_list)
```

**Sample Output:**

```bash
Sorted List :  [1, 2, 3, 4, 5]
```

---

## Program 7: Merge Two Lists

```python
list1 = [1, 2, 3]
list2 = [4, 5, 6]

merged_list = list1 + list2

print("Merged List : ", merged_list)
```

**Sample Output:**

```bash
Merged List :  [1, 2, 3, 4, 5, 6]
```
