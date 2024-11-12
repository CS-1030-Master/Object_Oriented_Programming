class Student:
    school_name = "Weber State University"  # Class attribute shared by all instances
    #constructor initializer
    #attributes
    def __init__(self, first_name, last_name, grade):
        self.first_name = first_name
        self.last_name = last_name
        self.grade = grade
        self.email = first_name + last_name + '@weber.edu'
    
    def print_student_data(self):
        print (f"Student info \n",
               f"\tFirst Name: {self.first_name} \n",
               f"\tLast Name: {self.last_name} \n",
               f"\tGrade: {self.grade}\n",
               f"\tEmail: {self.email}",
               f"\tSchool: {Student.school_name}")
    
    def change_grade(self, new_grade_level):
        self.grade = new_grade_level
    
    def __str__(self):
        # The __str__ method provides a user-friendly string representation of the object.
        # This is called when we use print() on an instance of the class.
        return (f"Student: {self.first_name} {self.last_name}, "
            f"Grade: {self.grade}, Email: {self.email}")

        
#jay_pike is an instance of the student class
jay_pike = Student("Jay", "Pike", "Sophomore") #Object of the student class
jane_doe = Student("Jane", "Doe", "Senior") #object of the student class
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
