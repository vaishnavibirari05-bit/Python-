"""
MATCH_CASE : 
     The match-case statement in Python is a clean way to compare a variable's value against multiple possibilities, acting as a more readable alternative to a long chain of if-elif-else statements.
     Introduced in Python 3.10, it is often called Structural Pattern Matching because it can check both the value and the shape of your data.
     We should choose Python's match-case statement when you are performing structural pattern matching or checking a single variable/object against many exact literal values or shapes. 

    syntax:
        match expression:
            case pattern_1:
                //LOC
            case pattern_2:
                //LOC
            case _:
                //LOC
"""
# Grade
# grade = input("Enter the Grade :-")
# match grade:
#  case "A":
#     print("Excellent")
#  case "B":
#     print("Very Good")
#  case "C":
#     print("Good")
#  case "D":
#     print("pass")
#  case "F":
#       print("Fail")
#  case _:
#       print("Invalid input..!")


# Quarters
# month = input("Enter the month :-")
# match month:
#     case "January"|"february"|"March":
#         print("Quarter 1")
#     case "April"|"May"|"June":
#         print("Quarter 2")
#     case "July"|"augest"|"september":
#         print("Quarter 3")
#     case "octobar"|"november"|"december":
#         print("Quarter 4")
#     case _:
#         print("invalid input")


# Operator
# a = int(input("Enter the first Number:-"))
# b = int(input("Enter the second number:-"))
# operator = input("enter the operator(+,-,/,*,//,**,%):-")
# match operator:
#     case "+":
#         print("Addition of",a+b)
#     case "-":
#         print("Substraction of",a-b)
#     case "/":
#         print("Division of",a/b)
#     case "*":
#         print("Multipication of",a*b)
#     case"//":
#         print("Floor division of",a//b)
#     case"**":
#         print("Exponentiation of",a**b)
#     case"%":
#         print("Modulus of",a%b)


# WeakDays
# day = int(input("Enter the days 1-7 :-"))
# match day:
#     case 1:
#         print("Monday")
#     case 2:
#         print("Tuesday")
#     case 3:
#         print("Wednesday")
#     case 4:
#         print("Thursday")
#     case 5:
#         print("Friday")
#     case 6:
#         print("Saturday")
#     case 7:
#         print("Sunday")




# clr = input("Enter the Colour")
# match clr:
#     case "Red":
#         print("STOP")
#     case "yellow":
#         print("READY TO GO ")
#     case "green":
#         print("GO")
#     case _:
#         print("Invalid Input")



# day = int(input("Enter the Day: "))
# match day:
#     case 1 :
#         print('Monday')
#     case 2 :
#         print('Tuesday')
#     case 3 :
#         print('Wednesday')
#     case 4 :
#         print('Thursday')
#     case 5 :
#         print('Friday')
#     case 6 :
#         print('Saturday')
#     case 7 :
#         print('Sunday')
#     case _:
#         print("Invalid Day")
    
       

# month = input("Enter the month: ")
# match month:
#     case "january"|"February"|"March":
#         print("Quarter 1")
#     case "April"|"may"|"june":
#         Print("Quarter 2")
#     case "july"|"august"|"september":
#         print("Quarter 3")
#     case "october"|"november"|"december":
#         print("Quarter 4")



# grade = input("Enter the Grade: ")
# match grade:
#     case "A":
#         print("Excellent")
    
#     case "B":
#         print("Very Good")
    
#     case "C":
#         print("Good")
    
#     case "D":
#         print("Average")
    
#     case "E":
#         print("Poor")
    
#     case "F":
#         print("Fail")
    
#     case _:
#         print("Invalid Input")
   


# marks = int(input("Enter the marks: "))
# match marks:
#     case marks if marks >= 90 and marks <= 0:
#         print("Invalid marks")
#     case marks if marks >= 90:
#         print("Grade-A")
#     case marks if marks >= 80 :
#         print("Grade-B")
#     case marks if marks >= 70 :
#         print("Grade-C")
#     case marks if marks >= 60 :
#         print("Grade-D")
#     case marks if marks >= 35:
#         print("Grade-E")
#     case marks if marks <= 35:
#         print("Failed")



# a = 5
# b = 4
# opr = input("Enter the operator (+, -, *, /, **, //, %): ")
# match opr:
#     case '+':
#         print(f"addition of a + b is {a+b}")
#     case '-':
#         print(f"Subtraction of a - b is {a-b}")
#     case '*':
#         print(f"Multiplication of a * b is {a*b}")
#     case '/':
#         print(f"Dividation of a / b is {a/b}")
#     case '**':
#         print(f"Exponential of a ** b is {a**b}")
#     case '//':
#         print(f"Floor_Division of a // b is {a//b}")
#     case '%':
#         print(f"Modular of a % b is {a%b}")



# char = input("Enter the char: ")
# match char:
#     case 'a'|'e'|'i'|'o'|'u':
#         print("Vowels")
#     case 'b' | 'c' | 'd' | 'f' | 'g' | 'h' | 'j' | 'k' | 'l' | 'm' | 'n' | 'p' | 'q' | 'r' | 's' | 't' | 'v' | 'w' | 'x' | 'y' | 'z':
#         print("Constant")
#     case _:
#         print("Invalid Input")



# balance = 5000

# print("===== ATM MENU =====")
# print("1. Check Balance")
# print("2. Deposit")
# print("3. Withdraw")
# print("4. Exit")

# choice = int(input("Enter your choice: "))

# match choice:

#     case 1:
#         print("Your current balance is:", balance)

#     case 2:
#         amount = float(input("Enter deposit amount: "))

#         if amount > 0:
#             balance += amount
#             print("Amount deposited successfully!")
#             print("Updated balance:", balance)
#         else:
#             print("Please enter a valid amount.")

#     case 3:
#         amount = float(input("Enter withdrawal amount: "))

#         if amount <= 0:
#             print("Please enter a valid amount.")
#         elif amount <= balance:
#             balance -= amount
#             print("Withdrawal successful!")
#             print("Remaining balance:", balance)
#         else:
#             print("Insufficient balance!")

#     case 4:
#         print("Thank you for using our ATM!")

#     case _:
#         print("Invalid choice!")




