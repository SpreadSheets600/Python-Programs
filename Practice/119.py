count = int(input("Enter Number Of Students : "))
attendance = {}

for index in range(1, count + 1):
    name = input(f"Enter Student {index} Name : ")
    status = input(f"Enter Attendance For {name} : ")
    attendance[name] = status

present_count = 0

for status in attendance.values():
    if status.lower() == "present":
        present_count += 1

print(attendance)
print(f"Present Count : {present_count}")
