# Creating a Student Class

# Instructions:

# Define a Student class with attributes like name and age. Include a method to display student information.


class Student():
    def __init__(self,name,age) :
        self.name = name
        self.age = age

    def display_info(self):
        print(f"student name: {self.name}")
        print(f"student age: {self.age}")

student1 = Student("Joel",19)
student1.display_info()

