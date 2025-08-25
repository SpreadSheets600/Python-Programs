# Programming Assignment : Assignment 3

---

## Program 1 : Word frequency counter from a paragraph

```python
# Write a Python program that reads a paragraph from the user and prints the frequency of each word in it.

paragraph = input("Enter A Pragraph : ")
splitParagraph = paragraph.split(" ")

wordCount = {}

for word in splitParagraph:
    if word in wordCount.keys():
        wordCount[word] += 1
        
    else:
        wordCount[word] = 1

print("Freequency Of Words ~ ")

for word, count in wordCount.items():
    print(f"{word} : {count}")


```

OUTPUT (example):

```bash
Enter A Pragraph : hello world hello
Freequency Of Words ~ 
hello : 2
world : 1
```

---

## Program 2 : Caesar cipher — shift each alphabet character by 3

```python
# Write a Python program to encrypt a string by shifting each character by 3 positions in the alphabet. (For example: A → D, B → E, X → A, etc.)

text = input("Enter A String : ")

result = ""

for char in text:
    if char.islower():  # Lowercase Letters
        pos = ord(char) - ord("a")  # Position Of Letter ( 0 - 25 )
        pos = (pos + 3) % 26  # Shift By 3, Warp Around With Modulas

        newChar = chr(pos + ord("a"))  # Convert Back To Letter

        result += newChar

    elif char.isupper():  # Uppercase Letters
        pos = ord(char) - ord("A")
        pos = (pos + 3) % 26

        newChar = chr(pos + ord("A"))

    else:
        result += char

print("Encrypted Text : ", result)


```

OUTPUT (example):

```bash
Enter A String : Hello, World!
Encrypted Text :  Khoor, Zruog!
```

---

## Program 3 : Remove punctuation from a string and count words

```python
# Write a Python program to remove all punctuation (.,?!;: etc.) from a string and count the number of words.

import string

text = input("Enter A String : ")

cleanText = ""

for char in text:
    if char not in string.punctuation:
        cleanText += char

words = cleanText.split()
wordCount = len(words)

print("Text Without Puntuation : ", cleanText)
print("Numbe Of Words : ", wordCount)


```

OUTPUT (example):

```bash
Enter A String : Hello, world! This is great.
Text Without Puntuation :  Hello world This is great
Numbe Of Words :  5
```

---

## Program 4 : Find and print the longest word in a sentence

```python
# Write a Python function that finds and prints the longest word in a given sentence.

text = input("Enter A Sting : ")
text = text.split()

lenCount = 0
longestWord = ""

for word in text:
    if len(word) > lenCount:
        longestWord = word
        lenCount = len(word)

print("Longest Word : ", longestWord)
print("Length Of Word : ", lenCount)


```

OUTPUT (example):

```bash
Enter A Sting : Find the longest word in this sentence
Longest Word :  longest
Length Of Word :  7
```

---

## Program 5 : Password strength checker

```python
# Q5. Write a Python program to check whether a password is strong or weak.
# Conditions for strong password:

# At least 8 characters
# Contains at least one uppercase letter
# Contains at least one lowercase letter
# Contains at least one digit
# Contains at least one special character (@, #, $, %, &, *)

password = input("Enter Password : ")

oneUppercase = oneLowercase = oneDigit = oneSpecialChar = False

for char in password:
    if char.islower():
        oneLowercase = True

    elif char.isupper():
        oneUppercase = True

    elif char.isdecimal():
        oneDigit = True

    elif not char.isalnum():
        oneSpecialChar = True

if (oneUppercase and oneLowercase and oneDigit and oneSpecialChar) is True and len(password) >= 8:
    print("Password Is Strong!")

else:
    print("Password Is Weak!")


```

OUTPUT (examples):

```bash
Enter Password : Abc@1234
Password Is Strong!

Enter Password : password123
Password Is Weak!
```

---

## Program 6 : Count vowels, consonants, digits and special characters in a string

```python
# Q6.Write a program that takes a string and counts:

# Number of vowels
# Number of consonants
# Number of digits
# Number of special characters

text = input("Enter A Sting : ")

vowels = "aeiouAEIOU"
vowelCount = 0

consonantCount = 0
specialCount = 0
digitCount = 0

for char in text:
    if char.isalpha():
        if char in vowels:
            vowelCount += 1
        else:
            consonantCount += 1

    elif char.isdigit():
        digitCount += 1

    else:
        specialCount += 1

print("Number Of Vowels : ", vowelCount)
print("Number Of Consonants : ", consonantCount)

print("Number Of Digits : ", digitCount)
print("Number Of Special Characters : ", specialCount)


```

OUTPUT (example):

```bash
Enter A Sting : Hello123!
Number Of Vowels :  2
Number Of Consonants :  3
Number Of Digits :  3
Number Of Special Characters :  1
```

---

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
