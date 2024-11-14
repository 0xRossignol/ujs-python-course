tmp = input('请输入单词').split()
set_words = set(tmp)

# 按字母升序排序
sorted_words = sorted(set_words)

# 打印结果
print(" ".join(sorted_words))
