def create_dict_from_lists(list1: list, list2: list) -> dict:
    # 使用zip将两个列表配对，创建字典
    result_dict = dict(zip(list1, list2))
    return result_dict


# 输入两个列表
list1 = input("请输入第一个列表（用空格分隔）：").split()
list2 = input("请输入第二个列表（用空格分隔）：").split()

# 调用函数并输出结果
result = create_dict_from_lists(list1, list2)
print("生成的字典:", result)
