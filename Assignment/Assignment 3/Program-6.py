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
