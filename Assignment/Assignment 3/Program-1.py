# Write a Python program that reads a paragraph from the user and prints the frequency of each word in it.

paragraph = input("Enter A Pragraph : ")
splitParagraph = paragraph.split(" ")

wordCount = {}

for word in splitParagraph:
    if word in wordCount.keys():
        wordCount[word] += 1
        
    else:
        wordCount[word] = 1

print("Freequency Of Words ~ ")

for word, count in wordCount.items():
    print(f"{word} : {count}")
