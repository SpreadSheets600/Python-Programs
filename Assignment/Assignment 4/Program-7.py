employees = {
    101: {"name": "Alice", "department": "HR", "salary": 40000},
    102: {"name": "Bob", "department": "IT", "salary": 55000},
    103: {"name": "Charlie", "department": "Finance", "salary": 60000},
    104: {"name": "David", "department": "IT", "salary": 70000},
    105: {"name": "Eva", "department": "HR", "salary": 45000},
}


def print_department(dept):
    print(f"\nEmployees In {dept} Department :")

    found = False

    for emp_id, details in employees.items():
        if details["department"].lower() == dept.lower():
            print(
                f"ID : {emp_id}, Name : {details['name']}, Salary : {details['salary']}"
            )
            found = True

    if not found:
        print("No Employee Found!")


def max_salary_employee():
    max_emp = max(employees.items(), key=lambda x: x[1]["salary"])
    emp_id, details = max_emp

    print(
        f"\nEmployee With Maximum Salary :\nID : {emp_id}, Name : {details['name']}, "
        f"Department : {details['department']}, Salary : {details['salary']}"
    )


print_department("IT")
max_salary_employee()
