import datetime

# 获取当前时间
current_time = datetime.datetime.now()

# 获取星期几（英文）
weekday = current_time.strftime('%A')

# 获取当前月份的天数
days_in_month = (datetime.date(current_time.year, current_time.month + 1, 1) - datetime.date(current_time.year, current_time.month, 1)).days

# 格式化时间信息
time_str = current_time.strftime('%Y-%m-%d %H:%M:%S')
weekday_str = weekday
month_days_str = f"There are {days_in_month} days in this month."

# 测试
# print(time_str)
# print(weekday_str)
# print(month_days_str)

# 将信息写入文本文件
file_name = "time_info.txt"
with open(file_name, "w") as file:
    file.write(f"{time_str}\n")
    file.write(f"{weekday_str}\n")
    file.write(f"{month_days_str}\n")

# 从文件中读取内容并显示
with open(file_name, "r") as file:
    content = file.read()
    print(content)
