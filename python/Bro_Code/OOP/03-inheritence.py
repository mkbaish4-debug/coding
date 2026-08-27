# Inheritence = allows a class to have or inherit attributes and methods from another class
#               It helps with code reusability and extensibility
#               class child(parent)

class Animal:
    def __init__(self, name, is_alive):
        self.name = name
        self.is_alive = is_alive

    def sleep(self):
        print(f"{self.name} is asleep")

    def eat(self):
        print(f"{self.name} is eating")

class Dog(Animal):
    def speak(self):
        print("Woof!")

class Cat(Animal):
    def speak(self):
        print("Meow!")

class Mouse(Animal):
    def speak(self):
        print("Squeek!")

dog1 = Dog("Sheru", False)
cat1 = Cat("Kitty", True)
mouse1 = Mouse("Mickey", True)

dog1.speak()
cat1.speak()
mouse1.speak()

dog1.sleep()
cat1.eat()

