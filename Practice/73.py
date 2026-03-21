count = int(input("Enter Number Of Students : "))
students = {}

for index in range(1, count + 1):
    name = input(f"Enter Student {index} Name : ")
    marks = float(input(f"Enter {name} Marks : "))
    students[name] = marks

top_student = max(students, key=students.get)

print(f"Highest Marks Student : {top_student}")
print(f"Marks : {students[top_student]}")
