file_name = input("Enter File Name : ")
target_word = input("Enter Word To Search : ")

with open(file_name, "r") as file:
    for line in file:
        if target_word in line:
            print(line.rstrip())
