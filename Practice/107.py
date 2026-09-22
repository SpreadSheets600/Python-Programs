text = input("Enter A String : ")
upper_count = 0
lower_count = 0
digit_count = 0
special_count = 0

for char in text:
    if char.isupper():
        upper_count += 1
    elif char.islower():
        lower_count += 1
    elif char.isdigit():
        digit_count += 1
    else:
        special_count += 1

print(f"Uppercase : {upper_count}")
print(f"Lowercase : {lower_count}")
print(f"Digits : {digit_count}")
print(f"Special Characters : {special_count}")
