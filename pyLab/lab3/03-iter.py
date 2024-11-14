class FibonacciIterator:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.a, self.b = 1, 1  # 斐波那契数列的前两项
        self.index = 1  # 当前是第几项

    def __iter__(self):
        return self

    def __next__(self):
        # 获取当前斐波那契数
        if self.index < self.start:
            # 跳过前面的数直到start
            self.index += 1
            self.a, self.b = self.b, self.a + self.b
            return self.__next__()

        if self.index > self.end:
            raise StopIteration  # 超过结束项，停止迭代

        # 返回当前斐波那契数
        result = self.a
        self.a, self.b = self.b, self.a + self.b
        self.index += 1
        return result


# 创建迭代器，获取第 10 项到第 20 项的斐波那契数
fib_iter = FibonacciIterator(10, 20)

# 输出斐波那契数列的第10到第20项
for num in fib_iter:
    print(num)
