text = input("Enter A String : ")
result = ""

for char in text:
    code = ord(char)
    if 97 <= code <= 122:
        result += chr(code - 32)
    else:
        result += char

print(result)
