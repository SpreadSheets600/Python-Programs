text = input("Enter A String : ")
target = input("Enter A Character : ")
count = 0

for char in text:
    if char == target:
        count += 1

print(f"Occurrence : {count}")
