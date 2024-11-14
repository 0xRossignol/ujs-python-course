def calculate_bonus(profit):
    over_100000 = 100000 * 0.10
    over_200000 = 100000 * 0.075
    over_400000 = 200000 * 0.05
    over_600000 = 200000 * 0.03
    over_1000000 = 400000 * 0.015

    if profit <= 100000:  # 利润低于或等于10万，提成10%
        money = profit * 0.10
    elif profit <= 200000:  # 10万到20万之间，10% + 7.5%
        money = (over_100000 + (profit - 100000) * 0.075)
    elif profit <= 400000:  # 20万到40万之间，10% + 7.5% + 5%
        money = (over_100000 + over_200000 + (profit - 200000) * 0.05)
    elif profit <= 600000:  # 40万到60万之间，10% + 7.5% + 5% + 3%
        money = (over_100000 + over_200000 + over_400000 + (profit - 400000) * 0.03)
    elif profit <= 1000000:  # 60万到100万之间，10% + 7.5% + 5% + 3% + 1.5%
        money = (over_100000 + over_200000 + over_400000 + over_600000 + (profit - 600000) * 0.015)
    else:  # 超过100万，1%
        money = (over_100000 + over_200000 + over_400000 + over_600000 + over_1000000 + (profit - 1000000) * 0.01)

    return money


# 输入当月利润
profit = float(input("请输入当月利润（单位：元）："))

# 计算奖金
bonus = calculate_bonus(profit)

# 输出结果
print(f"应发放的奖金总数为：{bonus:.2f}元")
