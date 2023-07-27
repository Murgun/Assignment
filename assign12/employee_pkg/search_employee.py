def search_employee():
    try:
        search_name = input("Enter the employee name to search: ")
        with open("employees.txt", "r") as file:
            employees = file.readlines()
        found = False
        for emp in employees:
            if search_name in emp:
                print("Employee found: ", emp.strip())
                found = True
        if not found:
            print("Employee not found.")
    except Exception as e:
        print("Error: ", str(e))