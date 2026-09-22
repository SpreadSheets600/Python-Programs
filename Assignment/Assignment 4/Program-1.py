# Write a Python program to create a dictionary of 5 students with their roll numbers as keys and names as values. Print the dictionary.

students = {}

num = int(input("Enter The Number Of Students : "))

for i in range(num):
    rollNo = int(input("Enter The Roll No : "))
    name = input("Enter The Name : ")

    students[rollNo] = name

print(students)
