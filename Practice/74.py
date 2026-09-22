text = input("Enter A String : ")
frequency = {}

for char in text:
    frequency[char] = frequency.get(char, 0) + 1

print(frequency)
