path = "my.bat"
with open(path, "wb") as fp:
    fp.write(b"Xiaoming\nstudent")
with open(path, "rb") as fp:
    fp.seek(-7, 2)  # 移动到文件末尾
    last_bytes = fp.read(7)
    print(last_bytes)
