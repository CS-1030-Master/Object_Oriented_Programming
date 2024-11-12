# graduate_student.py
# Inheritance allows a class to inherit attributes and methods from another class.
# Here, GraduateStudent inherits from Student, gaining its attributes and methods.
# GraduateStudent can use Student's methods directly or override them to provide 
# more specialized behavior, demonstrating code reuse and extension of functionality.

from student import Student

class GraduateStudent(Student):
    def __init__(self, first_name, last_name, grade, student_id=None, degree_program="Masters"):
        # super() calls a method from the parent class, allowing the subclass to 
        # inherit and extend the functionality of the parent. It avoids code duplication 
        # and makes maintenance easier by inheriting any changes from the superclass.
        super().__init__(first_name, last_name, grade, student_id)
        self.degree_program = degree_program

    # Polymorphism allows methods to behave differently based on the object calling them.
    # In this example, the print_student_data method is defined in both Student and GraduateStudent classes.
    # When called, each object uses its own version of print_student_data, enabling different outputs 
    # for Student and GraduateStudent instances. This lets us treat objects of both types uniformly 
    # while leveraging their specific behaviors.
    
    # Overriding the print_student_data method for GraduateStudent
    def print_student_data(self):
        print(f"{self.first_name} {self.last_name}, Grade: {self.grade}, Program: {self.degree_program}")
