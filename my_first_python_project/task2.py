employee_data = {
    'shoaib': {'age': 42, 'salary': 50000},
    'usama': {'age': 25, 'salary': 60000},
    'nauman': {'age': 28, 'salary': 60000},
    'basit': {'age': 22, 'salary': 55000},
    'tahir': {'age': 25, 'salary': 500000}
}

def sort_employees(employee_dict):
    employees_list = [(name, details['age'], details['salary']) for name, details in employee_dict.items()]
    sorted_employees = sorted(employees_list, key=lambda x: (-x[2], x[1]))
    return sorted_employees

sorted_employees = sort_employees(employee_data)
for name, age, salary in sorted_employees:
    print(f"Name: {name}, Age: {age}, Salary: {salary}")