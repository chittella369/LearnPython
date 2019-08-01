#from Classes_And_Objects.Student import Student
from ClassesAndObjects import Student


student1 = Student("Aditya", "Data Science", 3.0, True)
student2 = Student("Radhika", "Human Resources", 10.0, False)
student3 = Student()

print(student1.studentname)
print(student2.gpa)

print(student1.on_honor_roll())
print(student2.on_honor_roll())