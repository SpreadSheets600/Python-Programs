rows = int(input("Enter Number Of Rows : "))
columns = int(input("Enter Number Of Columns : "))
matrix = []

for row in range(rows):
    current_row = [int(value) for value in input(f"Enter Row {row + 1} : ").split()]
    matrix.append(current_row)

transpose = []

for column in range(columns):
    current_row = []
    for row in range(rows):
        current_row.append(matrix[row][column])
    transpose.append(current_row)

for row in transpose:
    print(row)
