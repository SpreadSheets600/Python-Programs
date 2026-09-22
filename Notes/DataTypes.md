# Data Types In Python

---

## Immutable Data Types

Immutable data types are types whose values cannot be changed after they are created. Any operation that seems to modify them actually creates a new object.

### Immutable Data Types in Python

1. **Numbers** (int, float, complex)
2. **String** (`str`)
3. **Tuple** (`tuple`)
4. **Bytes** (`bytes`)

**Note:** Attempting to modify an immutable object will result in an error. For example, strings and tuples cannot be changed after creation.

---

```python
# Integer (int)
a = 10
print('Original a:', a)

a = a + 5  # This Creates a New Integer Object
print('Modified a:', a)

# String (str)
s = "hello"
print('Original s:', s)
try:
    s[0] = 'H'  # This Will Raise An Error
except TypeError as e:
    print('Error:', e)

# Tuple
t = (1, 2, 3)
print('Original tuple:', t)
try:
    t[0] = 10  # This Will Raise An Error
except TypeError as e:
    print('Error:', e)
```

---

OUTPUT :

```bash
Original a: 10
Modified a: 15
Original s: hello
Error: 'str' object does not support item assignment
Original tuple: (1, 2, 3)
Error: 'tuple' object does not support item assignment
```

---

## Mutable Data Types

Mutable data types are types whose values can be changed after they are created. Operations that modify these objects do not create a new object, but change the original object itself.

### Mutable Data Types in Python

1. **Set** (`set`)
2. **List** (`list`)
3. **Dictionary** (`dict`)

**Note:** You can modify, add, or remove elements from mutable objects.

---

```python
# List
lst = [1, 2, 3]
print('Original list:', lst)

lst[0] = 10  # Modifies The List In Place
print('Modified list:', lst)

# Dictionary
d = {'a': 1, 'b': 2}
print('Original dict:', d)

d['a'] = 100  # Modifies The Dictionary In Place
print('Modified dict:', d)

# Set
s = {1, 2, 3}
print('Original set:', s)

s.add(4)  # Modifies The Set In Place
print('Modified set:', s)
```
