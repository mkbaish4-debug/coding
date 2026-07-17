# Object = A collection of related data and functions or in other words
#          A container for data and methods that work on that data. or in other words.
#          A collection of relative attributes (variables) and methods (functions)
           #          Can be used to mimic real world objects (coffee cup, phones, books, etc.)
#          You need a "class" to create many objects
# class = It is a blueprint to create objects.

# class Car:
#     def __init__(self, model, year, color, for_sale):
#         self.model = model
#         self.year = year
#         self.color = color
#         self.for_sale  = for_sale

# we can also import class
from Car import Car

car1 = Car("Lamborghini", 2024, "Blue", False)
car2 = Car("Ferrari", 2022, "red", True)
car3 = Car("Mustang", 2021, "Black", False)

car1.description()
