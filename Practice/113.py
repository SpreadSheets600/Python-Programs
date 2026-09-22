rows = int(input("Enter Number Of Rows : "))
columns = int(input("Enter Number Of Columns : "))
matrix_1 = []
matrix_2 = []

for row in range(rows):
    matrix_1.append([int(value) for value in input(f"Enter First Matrix Row {row + 1} : ").split()])

for row in range(rows):
    matrix_2.append([int(value) for value in input(f"Enter Second Matrix Row {row + 1} : ").split()])

result = []

for row in range(rows):
    current_row = []
    for column in range(columns):
        current_row.append(matrix_1[row][column] + matrix_2[row][column])
    result.append(current_row)

for row in result:
    print(row)
