class Student:

    class_year = 2025
    num_students = 0

    def __init__(self,name,age):
        self.name = name
        self.age = age
        Student.num_students +=1


student1 = Student("zeeshan",20)
student2 = Student("zain",19)


print(f"his name is {student1.name}")
print(f"he is {student1.age} years old")
print(Student.class_year)
print(f" there are {Student.num_students} students  in the list")
