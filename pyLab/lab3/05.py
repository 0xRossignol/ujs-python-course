import random

set_A, set_B = set(), set()
for i in range(10):
    set_A.add(random.randint(0, 10))
    set_B.add(random.randint(0, 10))

print("-----------set_A-----------")
print(set_A)
print(f'len: {len(set_A)}')
print(f'max: {max(set_A)}')
print(f'min: {min(set_A)}')
print("-----------set_B-----------")
print(set_B)
print(f'len: {len(set_B)}')
print(f'max: {max(set_B)}')
print(f'min: {min(set_B)}')
print("-----------others-----------")
print(f'交集：{set_A & set_B}')
print(f'并集：{set_A | set_B}')
print(f'差集：{set_A - set_B}')
