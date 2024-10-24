import math


class Dimension:
    def area(self):
        print("形状没定，无法计算面积！")


class Triangle(Dimension):
    def __init__(self, base: float, height: float):
        self.base = base
        self.height = height

    def area(self) -> float:
        return 0.5 * self.base * self.height


class Circle(Dimension):
    def __init__(self, radius: float):
        self.radius = radius

    def area(self) -> float:
        return math.pi * (self.radius ** 2)


class Rectangle(Dimension):
    def __init__(self, height: float, width: float):
        self.height = height
        self.width = width

    def area(self):
        return self.height * self.width


test1 = Triangle(10, 10)
print(test1.area())

test2 = Circle(2)
print(test2.area())

test3 = Rectangle(2, 4)
print(test3.area())
