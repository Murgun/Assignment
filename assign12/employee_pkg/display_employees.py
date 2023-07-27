def display_employees():
    try:
        with open("employees.txt", "r") as file:
            employees = file.readlines()
        if employees:
            print("Employee Information:")
            for emp in employees:
                print(emp.strip())
        else:
            print("No employees found.")
    except Exception as e:
        print("Error: ", str(e))