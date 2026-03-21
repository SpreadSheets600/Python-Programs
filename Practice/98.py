file_name = input("Enter File Name : ")
data = input("Enter Data To Append : ")

with open(file_name, "a") as file:
    file.write(data + "\n")

print("Data Appended")
