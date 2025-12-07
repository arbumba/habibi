"""
class Student:
    count = 0
    def __init__(self, height = 157.5):
        self.height = height
        Student.count += 1
    def grow(self, height = 1):
        self.height += height

firstStudent = Student(firstStudent.count)
secondStudent = Student(height = 156, secondStudent.count)
Ivan = Student(height = 154.67), Ivan.count
print(Ivan.height, "cm")
Ivan.grow(height = -1)
print(firstStudent.height, "cm")
print(secondStudent.height, "cm")
print("Ivan is shrinking,", Ivan.height, "cm")
print("Student amount -", Student.count)
"""

class Student:
    def __init__(self, name = None):
        self.name = name
    def __str__(self):
        return f"I'm a student, my name is {self.name}"

Sofia = Student(name = "Sofia")
Ivan = Student(name = "Ivan")
print(Sofia)
print(Ivan)