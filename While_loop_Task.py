# 1. Fibonacci Series using While Loop
# n = int(input("Enter the number of terms: "))

# a = 0
# b = 1
# i = 1

# while i <= n:
#     print(a, end=" ")
#     c = a + b
#     a = b
#     b = c
#     i += 1

# 2. Reverse a Number using While Loop
# n = int(input("Enter a number: "))

# rev = 0

# while n > 0:
#     digit = n % 10
#     rev = rev * 10 + digit
#     n = n // 10

# print("Reverse number:", rev)

# 3. Palindrome String using While Loop
# s = input("Enter a string: ")

# rev = ""
# i = len(s) - 1

# while i >= 0:
#     rev = rev + s[i]
#     i -= 1

# if s == rev:
#     print("Palindrome")
# else:
#     print("Not Palindrome")

# 4. Palindrome Integer using While Loop
# n = int(input("Enter a number: "))

# temp = n
# rev = 0

# while temp > 0:
#     digit = temp % 10
#     rev = rev * 10 + digit
#     temp = temp // 10

# if n == rev:
#     print("Palindrome Number")
# else:
#     print("Not Palindrome Number")

# 5. Armstrong Number using While Loop
# n = int(input("Enter a number: "))

# temp = n
# digits = len(str(n))
# total = 0

# while temp > 0:
#     digit = temp % 10
#     total = total + digit ** digits
#     temp = temp // 10
# if n == total:
#     print("Armstrong Number")
# else:
#     print("Not Armstrong Number")

# 6. Prime Number or Not using While Loop
# n = int(input("Enter a number: "))

# i = 2
# is_prime = True

# if n <= 1:
#     is_prime = False
# else:
#     while i < n:
#         if n % i == 0:
#             is_prime = False
#             break
#         i += 1

# if is_prime:
#     print("Prime Number")
# else:
#     print("Not Prime Number")