text = input("Enter A String : ")
result = ""

for char in text:
    code = ord(char)
    if 65 <= code <= 90:
        result += chr(code + 32)
    else:
        result += char

print(result)
