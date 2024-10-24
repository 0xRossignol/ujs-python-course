# (1) 将元组写入文件
t = ("spring", "summer", "autumn")

with open('file2.txt', 'w') as f:
    for season in t:
        f.write(season + '\n')  # 每个元素单独放在一行中

# (2) 追加字符串 "winter"
with open('file2.txt', 'a') as f:
    f.write('winter\n')  # 追加到文件最后一行下面的一行

# (3) 打开文件并显示最后两行，添加异常处理
try:
    with open('file2.txt', 'r') as f:
        lines = f.readlines()  # 读取所有行
        last_two_lines = lines[-2:]  # 获取最后两行
        for line in last_two_lines:
            print(line.strip())  # 输出最后两行，去掉换行符
except FileNotFoundError:
    print("文件file2.txt打开失败！")
except Exception as e:
    print(f"打开文件时发生错误：{e}")
