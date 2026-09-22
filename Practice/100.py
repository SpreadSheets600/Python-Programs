file_name = input("Enter File Name : ")

try:
    with open(file_name, "r") as file:
        print(file.read())
except FileNotFoundError:
    print("File Does Not Exist")
