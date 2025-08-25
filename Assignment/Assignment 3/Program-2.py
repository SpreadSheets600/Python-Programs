# Write a Python program to encrypt a string by shifting each character by 3 positions in the alphabet. (For example: A → D, B → E, X → A, etc.)

text = input("Enter A String : ")

result = ""

for char in text:
    if char.islower():  # Lowercase Letters
        pos = ord(char) - ord("a")  # Position Of Letter ( 0 - 25 )
        pos = (pos + 3) % 26  # Shift By 3, Warp Around With Modulas

        newChar = chr(pos + ord("a"))  # Convert Back To Letter

        result += newChar

    elif char.isupper():  # Uppercase Letters
        pos = ord(char) - ord("A")
        pos = (pos + 3) % 26

        newChar = chr(pos + ord("A"))

    else:
        result += char

print("Encrypted Text : ", result)
