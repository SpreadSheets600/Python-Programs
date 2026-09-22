password = input("Enter Password : ")
has_uppercase = False
has_lowercase = False
has_digit = False
has_special = False

for char in password:
    if char.isupper():
        has_uppercase = True
    elif char.islower():
        has_lowercase = True
    elif char.isdigit():
        has_digit = True
    else:
        has_special = True

if len(password) >= 8 and has_uppercase and has_lowercase and has_digit and has_special:
    print("Valid Password")
else:
    print("Invalid Password")
