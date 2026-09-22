marks = []

for index in range(1, 6):
    marks.append(float(input(f"Enter Marks Of Subject {index} : ")))

total = sum(marks)
average = total / len(marks)
percentage = total / 5

print(f"Total : {total}")
print(f"Average : {average}")
print(f"Percentage : {percentage}")
