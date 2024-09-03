class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

class Organisation:
    def __init__(self):
        self.employees = {}

    def add_employee(self, name, age, salary):
        self.employees[name] = Employee(name, age, salary)

    def compute_total_salary(self):
        total_salary = sum(employee.salary for employee in self.employees.values())
        return total_salary

    def find_min_max_salary(self):
        min_salary = min(employee.salary for employee in self.employees.values())
        max_salary = max(employee.salary for employee in self.employees.values())
        return min_salary, max_salary

    def find_high_salary_employees(self):
        high_salary_employees = [employee.name for employee in self.employees.values() if employee.salary > 25000]
        return high_salary_employees

organisation = Organisation()

while True:
    print("\n1. Add Employee")
    print("2. Compute Total Salary")
    print("3. Find Min and Max Salary")
    print("4. Find Employees with Salary > 25000")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter employee name: ")
        age = int(input("Enter employee age: "))
        salary = int(input("Enter employee salary: "))
        organisation.add_employee(name, age, salary)
    elif choice == "2":
        total_salary = organisation.compute_total_salary()
        print("Total salary:", total_salary)
    elif choice == "3":
        min_salary, max_salary = organisation.find_min_max_salary()
        print("Minimum salary:", min_salary)
        print("Maximum salary:", max_salary)
    elif choice == "4":
        high_salary_employees = organisation.find_high_salary_employees()
        print("Employees with salary greater than 25000:", high_salary_employees)
    elif choice == "5":
        break
    else:
        print("Invalid choice. Please try again.")
