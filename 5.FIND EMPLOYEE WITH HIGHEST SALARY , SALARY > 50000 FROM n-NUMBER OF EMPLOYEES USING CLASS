class Employee:
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    def display(self):
        print("ID:", self.emp_id, "Name:", self.name, "Salary:", self.salary)


def main():
    n = int(input("Enter number of employees: "))
    employees = []
    for i in range(n):
        print("Enter details for employee", i + 1)
        eid = input("ID: ")
        name = input("Name: ")
        salary = float(input("Salary: "))
        employees.append(Employee(eid, name, salary))
    print("\n--- All Employee Details ---")
    for emp in employees:
        emp.display()

    # Calculate highest salary
    if employees:
        highest_emp = max(employees, key=lambda x: x.salary)
        print("\nHighest Salary:", highest_emp.salary, "by", highest_emp.name)

    # Find salary > 50000
    print("\n--- Employees with Salary > 50000 ---")
    for emp in employees:
        if emp.salary > 50000:
            emp.display()


if __name__ == "__main__":
    main()

