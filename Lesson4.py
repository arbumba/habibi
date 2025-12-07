class Shape:
    def __init__(self, color):
        self.color = color
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius
        self.name = "Circlum"
    def area(self):
        return 3.14 * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, color, width, height):
        super().__init__(color)
        self.width = width
        self.height = height
        self.name = "Rectanglum"
    def area(self):
        return  self.width * self.height

Circlum = Circle("red", 5)
print(f"This circle's name is {Circlum.name}")
print(f"This circle's radius is {Circlum.radius}")
print(f"The area of the circle is {Circlum.area()}")

print(" ")

Rectanglyus = Rectangle("blue", 5, 10)
print(f"This rectangle's name is {Rectanglyus.name}")
print(f"This rectangle's width is {Rectanglyus.width}, and the height is {Rectanglyus.height}")
print(f"The area of the rectangle is {Rectanglyus.area()}")
