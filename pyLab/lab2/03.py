text = ("spring", "summer", "autumn")
path = "file2.txt"
with open(path, "w") as fp:
    for item in text:
        fp.write(item + "\n")
with open(path, "a") as fp:
    fp.write("winter")
with open(path, "r") as fp:
    lines = fp.readlines()  # 读取所有行
    last_two_lines = lines[-2:]  # 获取最后两行
    for line in last_two_lines:
        print(line.strip())
