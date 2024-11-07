import math


class MyMath:
    def __init__(self, radius):
        """初始化时传入半径"""
        self.radius = radius

    def circle_circumference(self):
        """计算圆的周长"""
        return round(2 * math.pi * self.radius, 2)

    def circle_area(self):
        """计算圆的面积"""
        return round(math.pi * self.radius ** 2, 2)

    def sphere_surface_area(self):
        """计算球的表面积"""
        return round(4 * math.pi * self.radius ** 2, 2)

    def sphere_volume(self):
        """计算球的体积"""
        return round((4/3) * math.pi * self.radius ** 3, 2)


# 测试代码
radius = 5
mymath = MyMath(radius)

print(f"圆的周长: {mymath.circle_circumference()}")  # 输出圆的周长
print(f"圆的面积: {mymath.circle_area()}")          # 输出圆的面积
print(f"球的表面积: {mymath.sphere_surface_area()}")  # 输出球的表面积
print(f"球的体积: {mymath.sphere_volume()}")          # 输出球的体积
