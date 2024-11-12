class Student:
    school_name = "Weber State University"  # Class attribute shared by all instances
    all_students = [] #xlass attribute to store all instances

    #constructor initializer
    #attributes
    def __init__(self, first_name, last_name, grade, student_id=None):
        self.first_name = first_name
        self.last_name = last_name
        self.grade = grade
        self.student_id = self.format_student_id(student_id)
        self.email = first_name + last_name + '@weber.edu'

         # Add each instance to the all_students list
        Student.all_students.append(self)
    
    # Class method to create a student from a single name string
    # The @classmethod decorator in Python defines a method that belongs to the class itself, 
    # rather than to instances of the class. A classmethod takes the class (cls) as its first parameter, 
    # instead of an instance (self), allowing it to access and modify class-level data or create instances 
    # in alternative ways.
    @classmethod # python decorator
    def from_full_name(cls, full_name, grade, student_id):
        first_name, last_name = full_name.split()
        return cls(first_name, last_name, grade, student_id)

    def print_student_data(self):
        print (f"Student info \n",
               f"\tFirst Name: {self.first_name} \n",
               f"\tLast Name: {self.last_name} \n",
               f"\tGrade: {self.grade}\n",
               f"\tEmail: {self.email}\n",
               f"\tStudent ID: {self.student_id}\n",
               f"\tSchool: {Student.school_name}")
    
    def change_grade(self, new_grade_level):
        self.grade = new_grade_level
    
    def __str__(self):
        # The __str__ method provides a user-friendly string representation of the object.
        # This is called when we use print() on an instance of the class.
        return (f"Student: {self.first_name} {self.last_name}, "
            f"Grade: {self.grade}, Email: {self.email}, Student ID {self.student_id}")
    
    # @staticmethod in Python is a decorator that defines a method that belongs to 
    # the class rather than an instance, but unlike @classmethod, it doesn’t take 
    # the class (cls) as its first parameter. Static methods act like regular functions 
    # within the class and do not have access to either instance-specific data (self) or 
    # class-level data (cls). They’re used for utility functions that make sense to group 
    # with the class but don’t need to interact with its state.

    @staticmethod #python decorator
    def is_valid_email(email):
        # Simple email validation (could be more complex)
        return "@" in email and "." in email
    
    @staticmethod
    def format_student_id(student_id):
        # Format student ID with a leading "STU-" prefix if it exists
        return f"WSU-{student_id}" if student_id else "No ID assigned"
    
    @classmethod
    def get_all_students(cls):
        # Class method to access the list of all students
        return cls.all_students

        
