text = input("Enter A String : ")
vowels = 0
consonants = 0
digits = 0
spaces = 0

for char in text:
    if char.lower() in "aeiou":
        vowels += 1
    elif char.isalpha():
        consonants += 1
    elif char.isdigit():
        digits += 1
    elif char == " ":
        spaces += 1

print(f"Vowels : {vowels}")
print(f"Consonants : {consonants}")
print(f"Digits : {digits}")
print(f"Spaces : {spaces}")
