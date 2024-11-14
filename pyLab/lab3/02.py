import random


target = random.choice(range(0, 101, 2))

while True:
    guess = int(input("输入一个偶数"))
    if guess == target:
        print("正确")
        break
    elif guess > target:
        print("太大")
    elif guess < target:
        print("太小")
