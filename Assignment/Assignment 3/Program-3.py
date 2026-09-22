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
