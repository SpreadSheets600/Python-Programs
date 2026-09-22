# Write a Python function that finds and prints the longest word in a given sentence.

text = input("Enter A Sting : ")
text = text.split()

lenCount = 0
longestWord = ""

for word in text:
    if len(word) > lenCount:
        longestWord = word
        lenCount = len(word)

print("Longest Word : ", longestWord)
print("Length Of Word : ", lenCount)
