# Level 1: Very Basic (1–10)
# 1. Write a program to print numbers from 1 to 10
# for i in range(1,10):
#     print(i)

# 2. Write a program to print numbers from 1 to 20.

# for i in range(1,20):
#     print(i)

# 3. Write a program to print numbers from 10 to 1.
# for i in range(10,1,-1):
#     print(i)

# 4. Write a program to print all even numbers from 1 to 20.
# for i in range(1,20):
#     if  i % 2 == 0:
#      print("Even Number",i)

# 5. Write a program to print all odd numbers from 1 to 20.
# for i in range(1,20):
#     if i % 3 == 0:
#         print("ODD NUMBER",i)

# 6. Write a program to print numbers from 5 to 15.
# for i in range(1,16):
#     print(i)
# 7. Write a program to print numbers from 1 to 50.
# for i in range(1,51):
#     print(i)

# 8. Write a program to print the word "Hello" 5 times.
# for i in range(5):
#     print("Hello")

# 9. Write a program to print your name 10 times.
# for i in range(10):
#     print("Vaishnavi")

# 10. Write a program to print numbers from 20 to 10 in reverse order.
# for i in range(20,10,-1):
#     print(" ",i)

# Level 2: range() Practice (11–20)

# 11. Write a program to print numbers from 1 to 5 using range().
# for i in range(1,6):
#     print(i)

# 12. Write a program to print numbers from 2 to 10.
# for i in range(1,11):
#     print(i)
# 13. Write a program to print multiples of 2 from 2 to 20.
# for i in range(1,21):
#     if i % 2 == 0:
#         print(i)

# 14. Write a program to print multiples of 5 from 5 to 50.
# for i in range(5,51):
#     if i % 5 == 0:
#         print(i)

# 15. Write a program to print numbers from 1 to 30 with a step of 3.
# for i in range(1,30,3):
#     print(i)

# 16. Write a program to print numbers from 10 to 100 with a step of 10.
# for i in range(10,101,10):
#     print(i)
# 17. Write a program to print numbers from 50 to 0 in reverse order.
# for i in range(50,0,-1):
#     print(i)
# 18. Write a program to print even numbers from 2 to 30.
# for i in range(2,30):
#     if i % 2 == 0:
#         print("Even No.:-",i)

# 19. Write a program to print odd numbers from 1 to 29.
# for i in range(1,30):
#     if i % 3 == 0:
#         print("ODD NUMBER:-",i)

# 20. Write a program to print numbers from 100 to 10, decreasing by 10
# for i in range(100,10,-10):
#     print("Decreasing Number:-",i)

# Level 3: Sum and Counting (21–30)

# 21. Write a program to find the sum of numbers from 1 to 10.
# sum = 0
# for i in range(1,11):
#     sum = sum + i
#     print("sum",sum)

# 22. Write a program to find the sum of numbers from 1 to 50.
# sum = 0
# for i in range(1,50):
#     sum = sum + i
#     print("sum",sum)

# 23. Write a program to find the sum of even numbers from 1 to 20.
# sum = 0
# for i in range(1,20):
#     if i % 2 == 0:
#         sum = sum + i
#         print("Sum of even number:-",sum)
  
# 24. Write a program to find the sum of odd numbers from 1 to 20.
# sum = 0
# for i in range(1,20):
#     if i % 3 == 0:
#         sum = sum + i
#         print(sum)

# 25. Write a program to calculate the sum of numbers from 1 to n, where the user enters n.
# n = int(input("Enter the sum number:-"))
# sum = 0
# for i in range(1,n + 1):
#     sum = sum + i
# print("sum of numbers from 1 to", n, "is:", sum)

# 26. Write a program to count numbers from 1 to 100.
# for i in range(1,101):
#     print(i)

# 27. Write a program to count even numbers from 1 to 50.
# for i in range(1,50):
#     if i % 2 == 0:
#         print("Even Number:-", i)

# 28. Write a program to count odd numbers from 1 to 50.
# for i in range(1,50):
#     if i % 3 == 0:
#         print("Odd number:-", i)
# 29. Write a program to find the product of numbers from 1 to 5.
# product = 1
# for i in range(1, 6):
#     product = product * i

# print("Product of numbers from 1 to 5 is:", product)

# 30. Write a program to calculate the factorial of a number entered by the user.
# n = int(input("Enter the number:-"))
# fact = 1
# for i in range(1, n +1):
#     fact = fact * i
# print("Factorial of:-", n, "is:", fact)


# Level 4: Basic Number Programs (31–40)
# 31. Write a program to print the multiplication table of 2.
# for i in range(1,21):
#     if i % 2 == 0:
#         print(i)
# 32. Write a program to print the multiplication table of a number entered by the user.
# num = int(input("Enter a number: "))

# for i in range(1, 11):
#     print(num, "x", i, "=", num * i)

# 33. Write a program to print the squares of numbers from 1 to 10.
# num = int(input("Enter a number: "))
# square = num * num
# print("Square =", square)

# 34. Write a program to print the cubes of numbers from 1 to 10.
# for i in range(1, 11):
#     print(i, "=", i ** 3)

# 35. Write a program to print the first 10 multiples of 3.
# for i in range(1, 11):
#     print(3 * i)

# 36. Write a program to print all numbers divisible by 3 from 1 to 50.
# for i in range(1, 51):
#     if i % 3 == 0:
#         print(i)
# 37. Write a program to print all numbers divisible by 5 from 1 to 100.
# for i in range(1, 101):
#     if i % 5 == 0:
#         print(i)
# 38. Write a program to print numbers divisible by both 3 and 5 from 1 to 100.
# for i in range(1, 101):
#     if i % 3 == 0 and i % 5 == 0:
#         print(i)

# 39. Write a program to print the first 10 natural numbers and their squares.
# for i in range(1, 11):
#     print(i, "->", i * i)

# 40. Write a program to find the sum of the multiplication table of 5 (from 5 × 1 to 5 × 10).
# sum = 0
# for i in range(1, 11):
#     sum = sum + (5 * i)
# print("Sum =", sum)

# Level 5: Strings and Simple Patterns (41–50)
# 41. Write a program to print each character of the string "Python" on a new line.


# 42. Write a program to count the characters in "Hello World" using a for loop.
# text = "Python"
# for ch in text:
#     print(ch)
# 43. Write a program to count the vowels in a string.
# text = input("Enter a string: ")
# count = 0

# for ch in text.lower():
#     if ch in "aeiou":
#         count += 1
# print("Number of vowels =", count)

# 44. Write a program to print each character of your name.
# name = "Vaishnavi"
# for ch in name:
#     print(ch)

# 45. Write a program to print the numbers in a list: [10, 20, 30, 40, 50].
# numbers = [10, 20, 30, 40, 50]
# for num in numbers:
#     print(num)

# 46. Write a program to find the sum of all elements in a list.
# numbers = [10, 20, 30, 40, 50]
# total = 0
# for num in numbers:
#     total += num
# print("Sum =", total)

# 47. Write a program to find the largest number in a list without using max().
# numbers = [10, 25, 8, 45, 32]
# largest = numbers[0]
# for num in numbers:
#     if num > largest:
#         largest = num
# print("Largest number =", largest)

# 48. Write a program to print this pattern:
# for i in range(1, 6):
#     print("*" * i)

# 49. Write a program to print this pattern:
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end="")
    print()



