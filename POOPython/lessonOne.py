# Example 1

class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def get_name(self):
        return self.name
           
    def get_age(self):
        return self.age
    
    def set_age(self, age):
        self.age = age
        
    def set_name(self, name):
        self.name = name    
    
    def bark(self):
        print("bark")
        
    def bite(self):
        print("nhack")
        
d = Dog("Tim",13)
print(type(d))
d.bark()
print(d.name)

# Example 2

class Student():
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade # 0 - 100
        
    def get_grade(self):
        return self.grade
    
class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []
        
    def add_student(self, student):
        if len(self.students) <self.max_students:
            self.students.append(student)
            return True
        return False
    
    def get_average_grade(self):
        average = 0
        for student in self.students:
            average += student.get_grade()
        return average/ len(self.students)
        
s1= Student("Tim",19 , 95)
s2= Student("Bill",19 , 75)
s3= Student("Gill",19 , 55)

course = Course("Science",3)

course.add_student(s1)
course.add_student(s2)
course.add_student(s3)

print(course.students[0].name)
print(course.get_average_grade())