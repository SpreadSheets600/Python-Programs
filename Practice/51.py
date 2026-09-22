sentence = input("Enter A Sentence : ")
words = sentence.split()
longest_word = ""

for word in words:
    if len(word) > len(longest_word):
        longest_word = word

print(f"Longest Word : {longest_word}")
