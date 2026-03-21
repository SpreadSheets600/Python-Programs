file_name = input("Enter File Name : ")

with open(file_name, "r") as file:
    for line in file:
        print(line.rstrip())
