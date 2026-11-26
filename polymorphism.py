# # 1. Animal Sounds (Method Overriding)

# class Animal:
#     def sound(self):
#         print("Animal makes a sound")

# class Dog(Animal):
#     def sound(self):
#         print("Dog says Bark")

# class Cat(Animal):
#     def sound(self):
#         print("Cat says Meow")

# d = Dog()
# c = Cat()

# d.sound()
# c.sound()


# # 2. Vehicle (Method Overriding)

# class Vehicle:
#     def start(self):
#         print("Vehicle is starting")

# class Car(Vehicle):
#     def start(self):
#         print("Car starts with a key")

# class Bike(Vehicle):
#     def start(self):
#         print("Bike starts with a button")

# c = Car()
# b = Bike()

# c.start()
# b.start()


# 3. Shape Area (Method Overriding)

# class Shape:
#     def area(self):
#         print("Calculating area")

# class Circle(Shape):
#     def area(self):
#         r = 5
#         print("Circle Area:", 3.14 * r * r)

# class Rectangle(Shape):
#     def area(self):
#         length = 10
#         breadth = 5
#         print("Rectangle Area:", length * breadth)

# c = Circle()
# r = Rectangle()

# c.area()
# r.area()


# # 4. Employee Salary (Method Overriding)

# class Employee:
#     def calculate_salary(self):
#         print("Employee salary")

# class Manager(Employee):
#     def calculate_salary(self):
#         print("Manager Salary: 50000")

# class Developer(Employee):
#     def calculate_salary(self):
#         print("Developer Salary: 40000")

# m = Manager()
# d = Developer()

# m.calculate_salary()
# d.calculate_salary()


# # 5. Payment System (Method Overriding)

# class Payment:
#     def pay(self):
#         print("Select payment method")

# class UPI(Payment):
#     def pay(self):
#         print("Payment using UPI")

# class Cash(Payment):
#     def pay(self):
#         print("Payment using Cash")

# u = UPI()
# c = Cash()

# u.pay()
# c.pay()


# # 6. Student and Teacher (Method Overriding)

# class Person:
#     def display_role(self):
#         print("I am a Person")

# class Student(Person):
#     def display_role(self):
#         print("I am a Student")

# class Teacher(Person):
#     def display_role(self):
#         print("I am a Teacher")

# s = Student()
# t = Teacher()

# s.display_role()
# t.display_role()


# # 7. Calculator (Method Overloading Using Default Arguments)

# class Calculator:
#     def add(self, a, b, c=0):
#         print("Addition:", a + b + c)

# obj = Calculator()

# obj.add(10, 20)
# obj.add(10, 20, 30)


# # 8. Polymorphism Using Function (Duck Typing)

# class Dog:
#     def sound(self):
#         print("Dog says Bark")

# class Cat:
#     def sound(self):
#         print("Cat says Meow")

# def make_sound(animal):
#     animal.sound()

# d = Dog()
# c = Cat()

# make_sound(d)
# make_sound(c)


# # 9. Food Ordering System (Method Overriding)

# class Food:
#     def prepare(self):
#         print("Preparing food")

# class Pizza(Food):
#     def prepare(self):
#         print("Preparing Pizza")

# class Burger(Food):
#     def prepare(self):
#         print("Preparing Burger")

# class Sandwich(Food):
#     def prepare(self):
#         print("Preparing Sandwich")

# p = Pizza()
# b = Burger()
# s = Sandwich()

# p.prepare()
# b.prepare()
# s.prepare()


# 10. Online Shopping (Method Overriding)

# class Product:
#     def product_details(self):
#         print("Product Information")

# class Electronics(Product):
#     def product_details(self):
#         print("Electronics: Laptop")

# class Clothing(Product):
#     def product_details(self):
#         print("Clothing: T-Shirt")

# class Grocery(Product):
#     def product_details(self):
#         print("Grocery: Rice")

# e = Electronics()
# c = Clothing()
# g = Grocery()

# e.product_details()
# c.product_details()
# g.product_details()