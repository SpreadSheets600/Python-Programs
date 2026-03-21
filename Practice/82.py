def count_vowels(text):
    count = 0

    for char in text.lower():
        if char in "aeiou":
            count += 1

    return count


text = input("Enter A String : ")
print(f"Vowel Count : {count_vowels(text)}")
