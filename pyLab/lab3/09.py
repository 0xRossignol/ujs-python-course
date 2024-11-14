import re
from collections import Counter

# 读取文件内容
with open("abstract.txt", "r") as file:
    text = file.read()

# 统计段落数
paragraphs = re.split(r'\n\s*\n', text.strip())
num_paragraphs = len(paragraphs)

# 统计行数
lines = text.splitlines()
num_lines = len(lines)

# 统计句数
sentences = re.split(r'[.!?]', text)
sentences = [sentence.strip() for sentence in sentences if sentence.strip()]
num_sentences = len(sentences)

# 统计单词数
words = re.findall(r'\b\w+\b', text.lower())  # 转为小写，避免区分大小写
num_words = len(words)

# 统计单词频率
word_freq = Counter(words)

# 打印统计结果
print(f"段落数: {num_paragraphs}")
print(f"行数: {num_lines}")
print(f"句数: {num_sentences}")
print(f"单词数: {num_words}")
print("单词频率:")
for word, freq in word_freq.items():
    print(f"{word}: {freq}")
