# Q5. Write a Python program to check whether a password is strong or weak.
# Conditions for strong password:

# At least 8 characters
# Contains at least one uppercase letter
# Contains at least one lowercase letter
# Contains at least one digit
# Contains at least one special character (@, #, $, %, &, *)

password = input("Enter Password : ")

oneUppercase = oneLowercase = oneDigit = oneSpecialChar = False

for char in password:
    if char.islower():
        oneLowercase = True

    elif char.isupper():
        oneUppercase = True

    elif char.isdecimal():
        oneDigit = True

    elif not char.isalnum():
        oneSpecialChar = True

if (oneUppercase and oneLowercase and oneDigit and oneSpecialChar) is True and len(password) >= 8:
    print("Password Is Strong!")

else:
    print("Password Is Weak!")
