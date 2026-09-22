file_name = "file_93.txt"

with open(file_name, "w") as file:
    for index in range(1, 6):
        file.write(f"Line {index}\n")

print(f"Data Written To {file_name}")
