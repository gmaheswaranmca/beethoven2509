import repo_api as repo

def menu():
    message = '''
The menu choices are
1 - Create Employee
2 - Read All Employees 
3 - Read By Id 
4 - Update 
5 - Delete 
6 - Exit / Logout
Your choice:'''
    choice = int(input(message))
    if choice == 1:
        name = input('Name:')
        employeeDict = {'name' : name}
        employee = repo.create_employee(employeeDict)
        print('Employee created successfully.', employee)
    elif choice == 2:
        employees = repo.read_all()
        print('Employees:')
        for employee in employees:
            print(employee)
    elif choice == 3:
        id = int(input('ID'))
        employee = repo.read_by_id(id)
        if employee == None:
            print('Employee not found')
        else:
            print(employee)
    elif choice == 4:
        id = int(input('ID:'))
        old_employee = repo.read_by_id(id)
        if old_employee == None:
            print('Employee Not Found.')
        else:
            print(old_employee)
            name = input('Name:')
            new_product_dict = {'id':id, 'name' : name }
            savedEmployee = repo.update(new_product_dict)
            print('Product Updated Successfully.', savedEmployee)
    elif choice == 5:
        id = int(input('ID:'))
        old_employee = repo.read_by_id(id)
        if old_employee == None:
            print('Employee Not Found.')
        else:
            print(old_employee)
            if input('Are you sure to delete(y/n)?') == 'y':
                repo.delete_by_id(id)
                print('Employee Deleted Successfully')
    return choice

def menus():
    print('Employee Management App')
    choice = menu()
    while choice != 6:
        choice = menu()
    print('Thank you for using app')

menus()