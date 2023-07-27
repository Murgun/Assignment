def delete_employee():
    try:
        search_name = input("Enter the name of the employee to delete: ")
        with open("employees.txt", "r") as file:
            employees = file.readlines()
        updated_data = []
        found = False
        for emp in employees:
            if search_name not in emp:
                updated_data.append(emp)
            else:
                found = True
        if found:
            with open("employees.txt", "w") as file:
                file.writelines(updated_data)
            print("Employee information deleted successfully.")
        else:
            print("Employee not found.")
    except Exception as e:
        print("Error: ", str(e))