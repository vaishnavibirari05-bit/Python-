# 1. Single Inheritance – Animal

# Create a parent class Animal with a method eat().
# - Create a child class Dog.
# - Add a method bark() in the Dog class.
# - Create an object and call both methods.

# class Animal():
#     def eat(self):
#         print("Animal is eating")


# class Dog(Animal):
#     def bark(self):
#         print("Dog is barking")


# class Cat(Animal):
#     def Meow(self):
#         print("Cat is meowing")

# d1 = Dog()
# d1.eat()
# d1.bark()

# d2 = Cat()
# d2.eat()
# d2.Meow()


# 2. Single Inheritance – Student

# Create a parent class Person with:
# - name
# - age
# Create a child class Student with:
# - roll_no
# - course
# Display all details using a method.

# class Person():
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# class Student(Person):
#     def __init__(self, name, age, roll_no, course):
#         super().__init__(name, age)
#         self.roll_no = roll_no
#         self.course = course


#     def display(self):
#         print("Name:-",self.name)
#         print("Age:-",self.age)
#         print("Roll Number:-",self.roll_no)
#         print("Course:-",self.course)

# a = Student("Vaishnavi", 21, 1, "python")
# a.display()



# 3. Single Inheritance – Vehicle

# Create a parent class Vehicle with:
# - brand
# - color
# Create a child class Car with:
# - model
# - price
# Display all car details.

# class Vehicle:
#     def __init__(self, brand, color):
#         self.brand = brand
#         self.color = color

# class Car(Vehicle):
#     def __init__(self, brand, color, model, price):
#         super().__init__(brand,color)
#         self.model = model
#         self.price = price

#     def display(self):
#         print("Brand:-",self.brand)
#         print("color:-",self.color)
#         print("model:-",self.model)
#         print("price:-",self.price)

# c1 = Car("volkswagen", "Black", "Virtus", "2500000")
# c1.display()


# 4. Multilevel Inheritance – School

# Create three classes:
# - School – school_name
# - Student – student_name, inherited from School
# - Marks – marks, inherited from Student
# Display all information using an object of the Marks class.


# class School():
#    def __init__(self,school_name):
#       self.school_name = school_name


# class Student(School):
#    def __init__(self,school_name, std_name):
#       super().__init__(school_name)
#       self.std_name = std_name

# class Marks(Student):
#    def __init__(self,school_name, student_name, marks):
#       super().__init__(school_name, student_name)
#       self.marks = marks

#    def display(self):
#     print("School Name:- ", self.school_name)  
#     print("Student Name:-", self.std_name)
#     print("Student Marks:-", self.marks)   


# m = Marks("JPSP", "Vaishnavi", 82)
# m.display()




