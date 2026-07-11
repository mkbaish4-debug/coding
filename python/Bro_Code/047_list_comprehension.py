# list comprehension = A consice way to create lists in python
#                      compact and easier to read than traditional loops
#                     [expression for value in iterable if condition]

# doubles = [x * 2 for x in range(11)]
# triples = [x * 3 for x in range(11)]
# squares = [z * z for z in range(11)]
# print(doubles)
# print(triples)
# print(squares)

# numbers = [1, 3, -11, -2, -1, 0, 3]
# positive_nums = [num for num in numbers if num > 0]
# negative_nums = [num for num in numbers if num < 0]
# print(positive_nums)
# print(negative_nums)

grades = [23, 34, 56, 78, 67, 89, 93, 96, 12, 56, 45, 11]
passing_grades = [grade for grade in grades if grade >= 33]
print(passing_grades)
