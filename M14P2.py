class Student:
    def __init__(self, first_name, last_name, district_code, credits):
        self.first_name = first_name
        self.last_name = last_name
        self.district_code = district_code
        self.credits = credits

    def compute_tuition(self):
        if self.district_code == "I":
            rate = 250.00
        else:
            rate = 500.00

        tuition = self.credits * rate
        return tuition

    def display_student(self):
        print(f"Student: {self.first_name} {self.last_name}")
        print(f"District Code: {self.district_code}")
        print(f"Credits: {self.credits}")

student1 = Student("Alice", "Brown", "I", 12)

student1.display_student()
print(f"Tuition Owed: ${student1.compute_tuition():.2f}")
