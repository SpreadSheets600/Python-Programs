source_file = input("Enter Source File Name : ")
target_file = input("Enter Target File Name : ")

with open(source_file, "r") as source:
    content = source.read()

with open(target_file, "w") as target:
    target.write(content)

print("File Copied")
