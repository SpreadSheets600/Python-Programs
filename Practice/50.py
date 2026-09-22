text = input("Enter A String : ")
result = ""

for char in text:
    if char != " ":
        result += char

print(result)
