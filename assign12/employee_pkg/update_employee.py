def update_employee():
    try:
        search_name = input("Enter the name of the employee to update: ")
        with open("employees.txt", "r") as file:
            employees = file.readlines()
        updated_data = []
        found = False
        for emp in employees:
            if search_name in emp:
                updated_emp_data = input("Enter updated employee information: ")
                updated_data.append(updated_emp_data + "\n")
                found = True
            else:
                updated_data.append(emp)
        if found:
            with open("employees.txt", "w") as file:
                file.writelines(updated_data)
            print("Employee information updated successfully.")
        else:
            print("Employee not found.")
    except Exception as e:
        print("Error: ", str(e))