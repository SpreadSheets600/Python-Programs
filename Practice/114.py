rows_1 = int(input("Enter First Matrix Rows : "))
columns_1 = int(input("Enter First Matrix Columns : "))
matrix_1 = []

for row in range(rows_1):
    matrix_1.append([int(value) for value in input(f"Enter First Matrix Row {row + 1} : ").split()])

rows_2 = int(input("Enter Second Matrix Rows : "))
columns_2 = int(input("Enter Second Matrix Columns : "))
matrix_2 = []

for row in range(rows_2):
    matrix_2.append([int(value) for value in input(f"Enter Second Matrix Row {row + 1} : ").split()])

if columns_1 != rows_2:
    print("Matrix Multiplication Is Not Possible")
else:
    result = []

    for row in range(rows_1):
        current_row = []
        for column in range(columns_2):
            total = 0
            for index in range(columns_1):
                total += matrix_1[row][index] * matrix_2[index][column]
            current_row.append(total)
        result.append(current_row)

    for row in result:
        print(row)
