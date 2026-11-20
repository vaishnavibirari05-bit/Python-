# class Student:
#     def __init__(self, name, roll_no, age):
#         self.name = name
#         self.roll_no = roll_no
#         self.age = age

#     def display(self):
#         print("Name:", self.name)
#         print("Roll No:", self.roll_no)
#         print("Age:", self.age)


# s1 = Student("Vaishnavi", 101, 21)
# s1.display()

# Q2. Mobile Class
# Create a Mobile class with brand, model and price
# class Mobile:
#     def __init__(self, brand, model, price):
#         self.brand = brand
#         self.model = model
#         self.price = price

#     def display(self):
#         print("Brand:", self.brand)
#         print("Model:", self.model)
#         print("Price:", self.price)


# m1 = Mobile("Samsung", "S24", 50000)
# m1.display()

# Q3. Car Class
# Create a Car class with brand, colour and speed. Create three objects
# class Car:
#     def __init__(self, brand, colour, speed):
#         self.brand = brand
#         self.colour = colour
#         self.speed = speed

#     def display(self):
#         print(self.brand, self.colour, self.speed)


# c1 = Car("BMW", "Black", 200)
# c2 = Car("Audi", "White", 180)
# c3 = Car("Tata", "Red", 150)

# c1.display()
# c2.display()
# c3.display()

# Q4. Rectangle Class
# Calculate the area using a method.

# class Rectangle:
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width

#     def area(self):
#         print("Area:", self.length * self.width)


# r1 = Rectangle(10, 5)
# r1.area()

# Q5. Circle Class
# Calculate the area of a circle.

# class Circle:
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         print("Area:", 3.14 * self.radius * self.radius)


# c1 = Circle(5)
# c1.area()

# Q6. Employee Class
# Calculate annual salary.

# class Employee:
#     def __init__(self, name, emp_id, salary):
#         self.name = name
#         self.emp_id = emp_id
#         self.salary = salary

#     def annual_salary(self):
#         print("Name:", self.name)
#         print("Employee ID:", self.emp_id)
#         print("Annual Salary:", self.salary * 12)


# e1 = Employee("Rahul", 101, 25000)
# e1.annual_salary()

# Q7. BankAccount Class
# Implement deposit and withdrawal

# class BankAccount:
#     def __init__(self, name, acc_no, balance):
#         self.name = name
#         self.acc_no = acc_no
#         self.balance = balance

#     def deposit(self, amount):
#         self.balance += amount
#         print("Deposited:", amount)

#     def withdraw(self, amount):
#         if amount <= self.balance:
#             self.balance -= amount
#             print("Withdrawn:", amount)
#         else:
#             print("Insufficient Balance")

#     def display(self):
#         print("Name:", self.name)
#         print("Account No:", self.acc_no)
#         print("Balance:", self.balance)


# b1 = BankAccount("Vaishnavi", 12345, 10000)

# b1.deposit(2000)
# b1.withdraw(3000)
# b1.display()

# Q8. Product Class
# Calculate the total bill

# class Product:
#     def __init__(self, name, price, quantity):
#         self.name = name
#         self.price = price
#         self.quantity = quantity

#     def total_bill(self):
#         total = self.price * self.quantity
#         print("Product:", self.name)
#         print("Total Bill:", total)


# p1 = Product("Laptop", 50000, 2)
# p1.total_bill()

# Q9. Student Marks
# Calculate total, percentage and result.

# class Student:
#     def __init__(self, name, m1, m2, m3):
#         self.name = name
#         self.m1 = m1
#         self.m2 = m2
#         self.m3 = m3

#     def result(self):
#         total = self.m1 + self.m2 + self.m3
#         percentage = total / 3

#         print("Name:", self.name)
#         print("Total:", total)
#         print("Percentage:", percentage)

#         if self.m1 >= 35 and self.m2 >= 35 and self.m3 >= 35:
#             print("Result: Pass")
#         else:
#             print("Result: Fail")


# s1 = Student("Rahul", 80, 75, 90)
# s1.result()

