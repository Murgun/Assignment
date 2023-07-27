import os

def add_employee():
    try:
        employee_data = input("Enter employee information (e.g., Name, ID, Position): ")
        with open("employees.txt", "a") as file:
            file.write(employee_data + "\n")
        print("Employee information added successfully.")
    except Exception as e:
        print("Error: ", str(e))