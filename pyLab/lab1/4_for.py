sum_total = 0
sum_odd = 0
sum_even = 0
for i in range(101):
    sum_total += i
    if i % 2 == 0:
        sum_even += i
    else:
        sum_odd += i
print(sum_total)
print(sum_odd)
print(sum_even)
