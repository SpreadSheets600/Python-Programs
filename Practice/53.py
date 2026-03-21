text_1 = input("Enter String 1 : ").replace(" ", "").lower()
text_2 = input("Enter String 2 : ").replace(" ", "").lower()

if sorted(text_1) == sorted(text_2):
    print("Anagrams")
else:
    print("Not Anagrams")
