import math


def not_a_circle(a : float, b : float, c : float) -> bool:
    return not (0 < c < a + b and 0 < a < b + c and 0 < b < a + c)


a, b, c = list(map(float, input().split()))
while not_a_circle(a, b, c):
    if not_a_circle(a, b, c):
        print("no a circle, input a new one")
        a, b, c = list(map(float, input().split()))
h = (a + b + c) / 2
s = math.sqrt(h * (h - a) * (h - b) * (h - c))
print(s)
