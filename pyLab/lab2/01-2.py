def fact(n: int) -> int:
    if n == 1:
        return 1
    return n * fact(n - 1)


n_input = int(input("输入n:"))
print(fact(n_input))
