rows = int(input("Enter Number Of Rows : "))

for row in range(1, rows + 1):
    print(" " * (rows - row) + "*" * row)
