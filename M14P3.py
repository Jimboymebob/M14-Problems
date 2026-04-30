class Student:
    def __init__(self, first_name, last_name, district_code, credits):
        self.first_name = first_name
        self.last_name = last_name
        self.district_code = district_code
        self.credits = credits

        #tuition rates
        self.rate_dict = {
            "I": 250.00,  # In district
            "O": 500.00,  # Out of district
            "X": 800.00,  # International
            "G": 250.00   # Reciprocity (same as I)
        }

    def compute_tuition(self):
        # Default to out-of-district if code not found
        rate = self.rate_dict.get(self.district_code, 500.00)
        return self.credits * rate

    def display_student(self):
        print(f"Student: {self.first_name} {self.last_name}")
        print(f"District Code: {self.district_code}")
        print(f"Credits: {self.credits}")


# Test with different students
student_I = Student("Tom", "Wilson", "I", 12)
student_O = Student("Sara", "Lee", "O", 12)
student_X = Student("Raj", "Patel", "X", 12)
student_G = Student("Emma", "Davis", "G", 12)

students = [student_I, student_O, student_X, student_G]

for s in students:
    s.display_student()
    print(f"Tuition Owed: ${s.compute_tuition():.2f}")
    print("-" * 30)
