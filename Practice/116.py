def count_letters(text):
    uppercase_count = 0
    lowercase_count = 0

    for char in text:
        if char.isupper():
            uppercase_count += 1
        elif char.islower():
            lowercase_count += 1

    return uppercase_count, lowercase_count


text = input("Enter A String : ")
uppercase_count, lowercase_count = count_letters(text)

print(f"Uppercase : {uppercase_count}")
print(f"Lowercase : {lowercase_count}")
