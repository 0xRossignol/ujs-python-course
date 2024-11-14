import random

ls = []
for _ in range(10):
    ls.append(random.randint(10, 100))
ls.sort()
print(ls)
aver = sum(ls) / len(ls)
print(f'平均数: {aver}')
print(f'大于平均数的个数: {len(list(filter(lambda x: x > aver, ls)))}')
