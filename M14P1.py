class Employee:
    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def display_employee(self):
        print(f"Employee: {self.first_name} {self.last_name}")
        print(f"Salary: ${self.salary:.2f}")

    def calculate_bonus(self, rate):
        bonus = self.salary * rate
        return bonus


# Test the class
emp1 = Employee("John", "Smith", 50000)

emp1.display_employee()

rate = float(input("Enter bonus rate (example 0.10 for 10%): "))
bonus = emp1.calculate_bonus(rate)

print(f"Bonus: ${bonus:.2f}")
