a = input('请输入a')
n = int(input('请输入n'))
result = sum([int(a * i) for i in range(1, n + 1)])
print(f"结果是: {result}")
