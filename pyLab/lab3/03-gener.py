def fibonacci_generator(start, end):
    a, b = 1, 1
    index = 1
    while index <= end:
        if index >= start:
            yield a  # 返回当前斐波那契数
        a, b = b, a + b
        index += 1


# 创建生成器，获取第 10 项到第 20 项的斐波那契数
fib_gen = fibonacci_generator(10, 20)

# 输出斐波那契数列的第10到第20项
for num in fib_gen:
    print(num)
