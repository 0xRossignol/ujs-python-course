cnt = 0
for i in range(101,201):
    flag = True
    for j in range(2, i):
        if i % j == 0:
            flag = False
            break
    if flag:
        if cnt % 10 == 0 and cnt != 0:
            print()
        print(i, end=" ")
        cnt += 1
