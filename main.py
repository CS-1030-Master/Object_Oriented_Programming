# Importing the Student class from the student module (File) to use in this program.
# This allows us to create and manipulate Student instances directly in main.py.
from student import Student
from graduate_student import GraduateStudent

#jay_pike is an instance of the student class
jay_pike = Student.from_full_name("Jay Pike", "Sophomore", 4567) #Object of the student class
jane_doe = GraduateStudent("Jane", "Doe", "Senior", 1234, "PhD") #object of the student class
waldo_wildcat = Student("Waldo", "Wildcat", "Senior")

jay_pike.print_student_data()
jane_doe.print_student_data()
waldo_wildcat.print_student_data()

jay_pike.change_grade("Junior")
jane_doe.change_grade("Graduated")
waldo_wildcat.change_grade("Freshman")

jay_pike.print_student_data()
jane_doe.print_student_data()
waldo_wildcat.print_student_data()

print(jay_pike)
print(jane_doe)
print(waldo_wildcat)

print(Student.is_valid_email("test@weber.edu"))  # True
print(Student.is_valid_email("invalid-email"))    # False

all_students = Student.get_all_students()
for student in all_students:
    student.print_student_data()
