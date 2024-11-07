class MyList:

    def __init__(self, data: list):
        self.data = data

    # 修改输出格式
    def __repr__(self):
        return f'{self.data}'

    def __add__(self, other):
        if isinstance(other, int):
            return MyList([x + other for x in self.data])
        if isinstance(other, MyList):
            return MyList([x + y for x, y in zip(self.data, other.data)])

    def __sub__(self, other):
        if isinstance(other, int):
            return MyList([x - other for x in self.data])
        if isinstance(other, MyList):
            return MyList([x - y for x, y in zip(self.data, other.data)])

    def __mul__(self, other):
        if isinstance(other, int):
            return MyList([x * other for x in self.data])
        if isinstance(other, MyList):
            return MyList([x * y for x, y in zip(self.data, other.data)])

    def __truediv__(self, other):
        if isinstance(other, int):
            return MyList([x / other for x in self.data])
        if isinstance(other, MyList):
            return MyList([x / y if y != 0 else float('inf') for x, y in zip(self.data, other.data)])


# 示例用法
my_list1 = MyList([1, 2, 3, 4])
my_list2 = MyList([10, 20, 30, 40])

# 加法
result_add = my_list1 + 5  # 对每个元素加 5
print(result_add)  # 输出: [6, 7, 8, 9]

# 减法
result_sub = my_list1 - 1  # 对每个元素减 1
print(result_sub)  # 输出: [0, 1, 2, 3]

# 乘法
result_mul = my_list1 * 2  # 对每个元素乘 2
print(result_mul)  # 输出: [2, 4, 6, 8]

# 除法
result_div = my_list1 / 2  # 对每个元素除 2
print(result_div)  # 输出: [0.5, 1.0, 1.5, 2.0]
