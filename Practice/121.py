import random
import string


length = int(input("Enter Password Length : "))
characters = string.ascii_letters + string.digits
password = ""

for _ in range(length):
    password += random.choice(characters)

print(password)
