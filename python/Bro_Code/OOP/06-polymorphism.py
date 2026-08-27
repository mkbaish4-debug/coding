# Polymorphism = Greek word that means to "have many forms or faces"
#         Poly = many
#         morph = forms
#         Two ways to achieve polymorphism
#         1. Inheritence = An object could be treated of the same class as the parent class
#         2. Duck typing = Object must have necessary methods/attributes

from abc import ABC, abstractmethod

class Shape:

    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

class Pizza(Circle):
    def __init__(self, radius, topping):
        super().__init__(radius)
        self.topping = topping

shapes = [Circle(4), Square(4), Triangle(3, 4), Pizza(15, "pepperoni")]

for shape in shapes:
    print(f"Area is: {shape.area()}")
