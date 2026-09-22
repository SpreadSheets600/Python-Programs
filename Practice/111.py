import string


text = input("Enter A String : ")
result = ""

for char in text:
    if char not in string.punctuation:
        result += char

print(result)
