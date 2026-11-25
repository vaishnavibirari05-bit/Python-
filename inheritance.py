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

# class Demo():

#      def __init__(self,name,city):
#           self.name = name
#           self.city = city
#           print("Cosntr of Parent --> ",name,city )


# class Day(Demo):

#      def __init__(self,name,city): 
#         super().__init__(name,city)
#         print("Name --> ",name,"City --> ",city)
         
    
# d = Day("Praful","goa")

# ---------------------------------------------------------------------------------------------------------------------------------------

# Create Hospital class with hospital_name and location. create a doctor child class with doctor_name and specialization :

# class Hospital:
#     def __init__(self, H_name, H_city):
#         self.name = H_name
#         self.city = H_city

# class Doctor(Hospital):
#     def __init__(self, H_name, H_city, d_name, d_specialization):
#         super().__init__(H_name, H_city)
#         self.dname = d_name
#         self.specialization = d_specialization

#     def display(self):
#         print("Hospital Name:", self.name)
#         print("City:", self.city)
#         print("Doctor Name:", self.dname)
#         print("Specialization:", self.specialization)

# d1 = Doctor("Orchid", "Jalgaon", "xyz", "abc")
# d1.display()

# ------------------------------------------------------------------------------------------------------------------------------------------

# Create a class Product with product_id and prodcut_name.create electronic_products with warranty_years.

# class Product():
    
#     def __init__(self, product_id, product_name):
#         self.id = product_id
#         self.name = product_name

# class Electronic_product(Product):

#     def __init__(self, product_id, product_name, warranty_year):
#         super().__init__(product_id, product_name)
#         self.warranty = warranty_year

#     def display(self):
#         print("Product Id: ",self.id)
#         print("Product Name: ",self.name)
#         print("Warranty Year: ",self.warranty)

# p = Electronic_product(123, "Laptop", "2-years")
# p.display()

# ----------------------------------------------------------------------------------------------------------------------------------------

# create two parent classes music player and camera. create a smartdevice child that inherits both.

# class MusicPlayer:
#     def play_music(self):
#         print("Playing music")

# class Camera:
#     def take_photo(self):
#         print("Taking photo")

# class SmartDevice(MusicPlayer, Camera):
#     pass

# # Usage
# device = SmartDevice()
# device.play_music()
# device.take_photo()

# -------------------------------------------------------------------------------------------------------------------------------------------

# Create Animal --> mammal --> Dog using multilevel inheritance.

# class Animal:
#     def eat(self):
#         print("Eating")

# class Mammal(Animal):
#     def walk(self):
#         print("Walking")

# class Dog(Mammal):
#     def bark(self):
#         print("Barking")


# dog = Dog()
# dog.eat()  
# dog.walk()  
# dog.bark() 

# ----------------------------------------------------------------------------------------------------------------------------------------------

# Create a school as parent and teacher, student and office_staff as child class 

# class School:
#     def attend(self):
#         print("Attending school")

# class Teacher(School):
#     def teach(self):
#         print("Teaching class")

# class Student(School):
#     def study(self):
#         print("Studying lessons")

# class OfficeStaff(School):
#     def manage(self):
#         print("Managing records")


# teacher = Teacher()
# teacher.attend()
# teacher.teach()

# student = Student()
# student.attend()
# student.study()

# staff = OfficeStaff()
# staff.attend()
# staff.manage()

# ----------------------------------------------------------------------------------------------------------------------------------------

# Create Athlet, person and student. create studentathlet inheriting athlet and student.

# class Person:
#     def breathe(self):
#         print("Breathing")

# class Athlete(Person):
#     def train(self):
#         print("Training")

# class Student(Person):
#     def study(self):
#         print("Studying")

# class StudentAthlete(Athlete, Student):
#     def balance(self):
#         print("Balancing sports and studies")


# sa = StudentAthlete()
# sa.breathe()  
# sa.train()    
# sa.study()  
# sa.balance()  

# -------------------------------------------------------------------------------------------------------------------------------------------

# create a parent class with parameterized initilizer and pass values from the child using super. 

# class Person:
#     def __init__(self, name):
#         self.name = name

# class Student(Person):
#     def __init__(self, name, grade):
#         super().__init__(name)  
#         self.grade = grade


# s = Student("Aarav", "A")
# print(s.name)  
# print(s.grade)

# -------------------------------------------------------------------------------------------------------------------------------------------
 
# create a parent method calculate_salary().override it in permanantEmployee and contractEmployee.

# class Employee:
#     def calculate_salary(self):
#         print("Base salary")

# class PermanentEmployee(Employee):
#     def calculate_salary(self):
#         print("Monthly fixed salary")

# class ContractEmployee(Employee):
#     def calculate_salary(self):
#         print("Hourly contract salary")


# p = PermanentEmployee()
# c = ContractEmployee()

# p.calculate_salary()  
# c.calculate_salary() 

# --------------------------------------------------------------------------------------------------------------------------------------------

# Create two parent classes with a method named info().inspect the child class MRO and explain which method is executed.

# class ParentA:
#     def info(self):
#         print("Info from ParentA")

# class ParentB:
#     def info(self):
#         print("Info from ParentB")

# class Child(ParentB, ParentA):
#     pass


# c = Child()
# c.info()      



