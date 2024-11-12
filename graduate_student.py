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

    def print_student_data(self):
        super().print_student_data()
        print(f"\tDegree Program: {self.degree_program}")
