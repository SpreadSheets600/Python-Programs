text = input("Enter A String : ")
clean_text = text.lower()
reversed_text = ""

for char in clean_text:
    reversed_text = char + reversed_text

if clean_text == reversed_text:
    print("Palindrome")
else:
    print("Not Palindrome")
