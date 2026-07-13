# variable scope = where the variable is visible and accessible
# scope resolution = (LEGB) local > enclosed > global > built-in

# def func1():
#     x = 1
#     print(x)
# # the scope of variable "x" is localwithin that function

# def func1():
#     x = 1
#     print(x)
#     def func2():
#        x = 2      # (so if x=2 is not present then x = 1 will be taken as that will enclosed scope)
#         print(x)
#     func2()

# func1()

# def func1():
#     x = 1
#     print(x)

# def func2():

#     print(x)

# x = 3

# func1()
# func2()
# if no local or enclosed then global

# from math import e

# e = 5
# print(e)
# if global is there built-in would not be taken

