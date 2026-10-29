# StudInfo = ['Rahul','Aman','Aryan']
# for ii in StudInfo:
#     for jj in ii:
#         if 'R' not in jj:
#             print(jj)


# ccc = [5,'xxxx','yy',4]
# for ele in ccc:
#     print(ele+2)

# stds = ['aryan', '123']

# if isinstance(stds, list):
#     stds.append(2)
#     print(stds)


# stds = ['aryan', '123']

# if isinstance(stds, list):
#     stds[1] = str(int(stds[1]) + 2)
#     print(stds)


# stds = ['aryan', '123', 5]

# if isinstance(stds, list):
#     stds[2] += 2
#     print(stds)

# nums = [10, 20, 30, 40, 50]

# i = 0
# while i < len(nums):
#     print(nums[i])
#     i += 1

# nums = [10, 20, 30, 40, 50]

# i = 0
# while True:
#     try:
#         print(nums[i])
#         i += 1
#     except IndexError:
#         break

# nums = [5, 10, 15, 20]

# i = 0
# total = 0

# while True:
#     try:
#         total += nums[i]
#         i += 1
#     except IndexError:
#         break

# print("Sum =", total)

# nums = [1, 2, 3, 4, 5, 6]

# i = 0
# while True:
#     try:
#         if nums[i] % 2 == 0:
#             print(nums[i])
#         i += 1
#     except IndexError:
#         break

# nums = [10, 15, 20, 25, 30]

# i = 0
# while True:
#     try:
#         if nums[i] % 2 != 0:
#             print(nums[i])
#         i += 1
#     except IndexError:
#         break

# nums = [1, 2, 3, 4, 5]

# i = 0
# while True:
#     try:
#         print(nums[i] ** 2)
#         i += 1
#     except IndexError:
#         break

# fruits = ["apple", "banana", "mango", "orange"]

# count = 0

# for item in fruits:
#     count += 1

# print("Count =", count)

# nums = [12, 45, 7, 89, 23]

# smallest = nums[0]
# i = 1

# while True:
#     try:
#         if nums[i] < smallest:
#             smallest = nums[i]
#         i += 1
#     except IndexError:
#         break

# print("Smallest =", smallest)


# mark_list = [4, 78, 96, 54, 94, 80]
# m1 = marks_list.copy()
# marks_list == m1

marks_list = [4, 78, 96, 54, 94, 80]


# m1 = marks_list.copy()
# print(marks_list == m1)

# marks_list.count(1)    It is used to print same as list
# print(marks_list)

# marks_list.append(1)      """append object to the end of the list"""
# print(marks_list)


# marks_list.insert(3,5)     ------insert objet br=efore index
# print(marks_list)


# marks_list.reverse()           -------it is used to reversed index
# print(marks_list)


marks_list.sort()
print(marks_list)