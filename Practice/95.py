file_name = input("Enter File Name : ")

with open(file_name, "r") as file:
    content = file.read()

lines = content.splitlines()
words = content.split()
characters = len(content)

print(f"Lines : {len(lines)}")
print(f"Words : {len(words)}")
print(f"Characters : {characters}")
