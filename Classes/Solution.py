class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def introduce(self):
        print(f"My name is {self.name} and I am {self.age} years old.")

# Create an object of the Person class
person = Person("John", 25)
person.introduce()

class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade
        
    def display_grade(self):
        print(f"My grade is {self.grade}.")

# Create an object of the Student class
student = Student("Jane", 18, "A")
student.introduce()
student.display_grade()

class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject
        
    def teach(self):
        print(f"I am teaching {self.subject}.")

# Create an object of the Teacher class
teacher = Teacher("Mr. Smith", 35, "Math")
teacher.introduce()
teacher.teach()
