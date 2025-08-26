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

OUTPUT :

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

OUTPUT :

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

OUTPUT :

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

OUTPUT :

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

OUTPUT :

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

OUTPUT :

```bash
Enter A Sting : Hello123!
Number Of Vowels :  2
Number Of Consonants :  3
Number Of Digits :  3
Number Of Special Characters :  1
```

---
