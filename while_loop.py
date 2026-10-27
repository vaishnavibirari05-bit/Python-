# # ==========================================
# # 11. Sum of Even Numbers from 1 to 20
# # ==========================================
# i = 2
# sum = 0

# while i <= 20:
#     sum += i
#     i += 2

# print("Sum =", sum)


# # ==========================================
# # 12. Sum of Odd Numbers from 1 to 20
# # ==========================================
# i = 1
# sum = 0

# while i <= 20:
#     sum += i
#     i += 2

# print("Sum =", sum)


# # ==========================================
# # 13. Product of Numbers from 1 to n
# # ==========================================
# n = int(input("Enter n: "))

# i = 1
# product = 1

# while i <= n:
#     product *= i
#     i += 1

# print("Product =", product)


# # ==========================================
# # 14. Print Squares from 1 to 10
# # ==========================================
# i = 1

# while i <= 10:
#     print(i, "Square =", i * i)
#     i += 1


# # ==========================================
# # 15. Print Cubes from 1 to 10
# # ==========================================
# i = 1

# while i <= 10:
#     print(i, "Cube =", i ** 3)
#     i += 1


# # ==========================================
# # 16. First 10 Multiples of 3
# # ==========================================
# i = 1

# while i <= 10:
#     print(3 * i)
#     i += 1


# # ==========================================
# # 17. First 20 Natural Numbers
# # ==========================================
# i = 1

# while i <= 20:
#     print(i)
#     i += 1


# # ==========================================
# # 18. Fibonacci Series (10 Terms)
# # ==========================================
# a = 0
# b = 1
# count = 1

# while count <= 10:
#     print(a)
#     c = a + b
#     a = b
#     b = c
#     count += 1


# # ==========================================
# # 19. Palindrome Number   
# # ==========================================
# n = int(input("Enter Number: "))

# temp = n
# rev = 0

# while n > 0:
#     digit = n % 10
#     rev = rev * 10 + digit
#     n //= 10

# if temp == rev:
#     print("Palindrome")
# else:
#     print("Not Palindrome")


# # ==========================================
# # 20. Armstrong Number
# # ==========================================
# n = int(input("Enter Number: "))

# temp = n
# sum = 0

# while n > 0:
#     digit = n % 10
#     sum += digit ** 3
#     n //= 10

# if temp == sum:
#     print("Armstrong Number")
# else:
#     print("Not Armstrong Number")


# # ==========================================
# # 21. Largest Digit in a Number
# # ==========================================
# n = int(input("Enter Number: "))

# largest = 0

# while n > 0:
#     digit = n % 10

#     if digit > largest:
#         largest = digit

#     n //= 10

# print("Largest Digit =", largest)


# # ==========================================
# # 22. Smallest Digit in a Number
# # ==========================================
# n = int(input("Enter Number: "))

# smallest = 9

# while n > 0:
#     digit = n % 10

#     if digit < smallest:
#         smallest = digit

#     n //= 10

# print("Smallest Digit =", smallest)


# # ==========================================
# # 23. Sum of Digits
# # ==========================================
# n = int(input("Enter Number: "))

# sum = 0

# while n > 0:
#     sum += n % 10
#     n //= 10

# print("Sum of Digits =", sum)


# # ==========================================
# # 24. Product of Digits
# # ==========================================
# n = int(input("Enter Number: "))

# product = 1

# while n > 0:
#     product *= n % 10
#     n //= 10

# print("Product =", product)


# # ==========================================
# # 25. Count Even Digits
# # ==========================================
# n = int(input("Enter Number: "))

# count = 0

# while n > 0:
#     digit = n % 10

#     if digit % 2 == 0:
#         count += 1

#     n //= 10

# print("Even Digits =", count)

def q01_print_1_to_10():
    """Q1. Print numbers from 1 to 10."""
    i = 1
    while i <= 10:
        print(i)
        i += 1


def q02_print_10_to_1():
    """Q2. Print numbers from 10 to 1."""
    i = 10
    while i >= 1:
        print(i)
        i -= 1


def q03_even_1_to_20():
    """Q3. Print even numbers from 1 to 20."""
    i = 2
    while i <= 20:
        print(i)
        i += 2


def q04_odd_1_to_20():
    """Q4. Print odd numbers from 1 to 20."""
    i = 1
    while i <= 20:
        print(i)
        i += 2


def q05_sum_1_to_10():
    """Q5. Find the sum of numbers from 1 to 10."""
    i = 1
    total = 0
    while i <= 10:
        total += i
        i += 1
    print("Sum =", total)


def q06_sum_1_to_n():
    """Q6. Accept n and find the sum from 1 to n."""
    n = int(input("Enter n: "))
    i = 1
    total = 0
    while i <= n:
        total += i
        i += 1
    print("Sum =", total)


def q07_multiplication_table():
    """Q7. Print the multiplication table of a number."""
    n = int(input("Enter a number: "))
    i = 1
    while i <= 10:
        print(n, "x", i, "=", n * i)
        i += 1


def q08_count_1_to_n():
    """Q8. Count from 1 to a number entered by the user."""
    n = int(input("Enter a number: "))
    i = 1
    while i <= n:
        print(i)
        i += 1


def q09_sum_even_1_to_n():
    """Q9. Find the sum of even numbers from 1 to n."""
    n = int(input("Enter n: "))
    i = 2
    total = 0
    while i <= n:
        total += i
        i += 2
    print("Sum of even numbers =", total)


def q10_sum_odd_1_to_n():
    """Q10. Find the sum of odd numbers from 1 to n."""
    n = int(input("Enter n: "))
    i = 1