sum_total, sum_odd, sum_even = 0, 0, 0
i = 0
while i <= 100:
    sum_total += i
    if i % 2 == 0:
        sum_even += i
    else:
        sum_odd += i
    i += 1
print(sum_total)
print(sum_odd)
print(sum_even)
