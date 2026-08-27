# class variables = It is shared among all instances of a class
#                   defined outside the constructor
#                   allow you to share data among all objects of a class

class Student:
    class_year = 2025
    num_of_students = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.num_of_students += 1

student1 = Student("Sayan", 19)
student2 = Student("Shahil", 19)
student3 = Student("Shiva", 19)
student4 = Student("Mayank", 19)

print(f"My graduating class of {Student.class_year} has {Student.num_of_students} students.")
print(student1.name)
print(student2.name)
print(student3.name)
print(student4.name)
