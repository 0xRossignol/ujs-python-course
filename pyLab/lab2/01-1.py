def fact(n: int) -> int:
    ans = 1
    if n == 1:
        return ans
    for i in range(1, n+1):
        ans *= i
    return ans


n_input = int(input("输入n:"))
print(fact(n_input))
