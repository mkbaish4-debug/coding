# super = It is a function that helps in extending the functionality of methods of parent class (super).
#         it also helps in defining the child class specific attributes
import math

class Shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled

    def describe(self):
        print(f"It is {self.color} and {"filled" if self.is_filled else "not filled"}")

class Circle(Shape):
    def __init__(self, color, is_filled, radius):
        super().__init__(color, is_filled)
        self.radius = radius

    def describe(self):
        print(f"It is a circle of area {math.pi * pow(self.radius, 2):.2f}cm^2")
        super().describe()

class Square(Shape):
    def __init__(self, color, is_filled, width):
        super().__init__(color, is_filled)
        self.width = width

    def describe(self):
        print(f"It is a square of area {pow(self.width, 2):.2f}cm^2")
        super().describe()

circle = Circle("red", True, 5)
square = Square("blue", False, 4)

circle.describe()
square.describe()



