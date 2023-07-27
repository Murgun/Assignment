from employee_pkg import add_employee, search_employee, update_employee, delete_employee, display_employees

if __name__ == "__main__":
    while True:
        print("\nEmployee Management System")
        print("1. Add Employee")
        print("2. Search Employee")
        print("3. Update Employee")
        print("4. Delete Employee")
        print("5. Display All Employees")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")
        
        if choice == "1":
            add_employee.add_employee()
        elif choice == "2":
            search_employee.search_employee()
        elif choice == "3":
            update_employee.update_employee()
        elif choice == "4":
            delete_employee.delete_employee()
        elif choice == "5":
            display_employees.display_employees()
        elif choice == "6":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")