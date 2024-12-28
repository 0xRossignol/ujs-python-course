import jieba
from collections import Counter


class Analyzer:
    url_prefix = "../data/visualizations/"
    # 英语停用词
    stop_words_en = [
        "the", "a", "an", "he", "she", "it", "they", "we", "you", "I", "me", "him", "her",
        "us", "them", "this", "that", "these", "those", "and", "but", "or", "nor", "for",
        "so", "yet", "in", "on", "at", "by", "with", "about", "against", "between", "under",
        "over", "through", "during", "before", "after", "is", "am", "are", "was", "were", "be",
        "been", "being", "have", "has", "had", "do", "does", "did", "will", "shall", "would",
        "should", "can", "could", "may", "might", "must", "not", "very", "just", "still", "also",
        "always", "even", "really", "too", "quite", "only", "for", "to", "of", "from", "as",
        "up", "down", "out", "off", "about", "how", "why", "What", "next", "new"
    ]
    # 中文停用词
    stop_words_cn = [
        '与', '能', '对不起', '比', '请', '为', '所以', '知道', '但是', '免费', '等',
        '对', '如同', '但', '来', '或', '怎么样', '非常', '哈', '虽然', '在', '她', '而',
        '这', '去', '想', '教程', '都', '到', '没有', '我', '一套', '呀', '是的', '那', '我们',
        '不过', '学习', '了', '什么', '你', '有', '会', '可以', '呢', '因为', '的', '每', '要',
        '跟', '它', '一种', '和', '你们', '看', '而且', '从', '并且', '啊', '只是', '说', '上',
        '也', '如果', '一个', '啦', '哦', '不是', '下', '做', '嘛', '它们', '还有', '怎么', '是',
        '些', '就', '并', '如', '他', '即使', '只', '学习'
        ]

    # 整合
    stop_words = stop_words_en + stop_words_cn

    def __init__(self, stopwords=None):
        """
        初始化分析器，支持传入自定义的停用词列表。
        """
        self.stopwords = stopwords if stopwords else set()

    def preprocess_text(self, text):
        """
        预处理文本，移除停用词并分词。
        """
        text = text.lower()
        words = jieba.lcut(text)
        words = [word for word in words if word not in self.stopwords and len(word.strip()) > 1]

        """
        将结果写入txt文件
        """
        path = "../data/processed/words.txt"
        with open(path, 'w', encoding='utf-8') as fp:
            cnt = 0
            for word in words:
                if cnt >= 15:
                    fp.write('\n')
                    cnt = 0
                fp.write(word + ' ')
                cnt += 1
        return words

    def calculate_word_frequency(self, words):
        """
        统计词频。
        """
        return Counter(words)


if __name__ == "__main__":
    from crawler import Crawler  # 假设模块1代码保存在 crawler.py

    # Step 1: 爬取标题
    url = "https://www.runoob.com/"
    crawler = Crawler()
    html = crawler.fetch_html(url)
    articles = crawler.parse_html(html)

    if articles:
        text = " ".join(article['title'] for article in articles)

        # Step 2: 初始化分析器
        stopwords = {"的", "在", "了", "是", "和", "也", "与", "等", "教程", "学习", "一个", "一种"}  # 可扩展停用词
        analyzer = Analyzer(stopwords=stopwords)

        # Step 3: 词汇分析和生成词云
        words = analyzer.preprocess_text(text)
        word_freq = analyzer.calculate_word_frequency(words)
        print("Word Frequency:", word_freq.most_common(10))  # 显示前10高频词

    else:
        print("No articles found for analysis.")
