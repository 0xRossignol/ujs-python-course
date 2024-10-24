import math


def calculate_area(a, b, c):
    # 计算半周长
    h = (a + b + c) / 2
    # 使用海伦公式计算面积
    area = math.sqrt(h * (h - a) * (h - b) * (h - c))
    return area


# 输入边长并检查有效性
while True:
    try:
        a = float(input("请输入三角形的边长 a: "))
        b = float(input("请输入三角形的边长 b: "))
        c = float(input("请输入三角形的边长 c: "))

        # 检查边长是否有效
        if a <= 0 or b <= 0 or c <= 0:
            print("边长必须大于0，请重新输入！")
            continue
        if a + b <= c or a + c <= b or b + c <= a:
            print("两边之和必须大于第三边，请重新输入！")
            continue

        # 计算面积
        area = calculate_area(a, b, c)
        print(f"三角形的面积为: {area:.2f}")  # 格式1: 保留两位小数
        print(f"三角形的面积为: {area:.3f}")  # 格式2: 保留三位小数
        break  # 输入合法，退出循环

    except ValueError:
        print("请输入有效的数字！")
