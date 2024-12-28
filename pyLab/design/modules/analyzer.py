import jieba
from collections import Counter


class Analyzer:
    url_prefix = "../data/visualizations/"

    def __init__(self, stopwords=None):
        """
        初始化分析器，支持传入自定义的停用词列表。
        """
        self.stopwords = stopwords if stopwords else set()

    def preprocess_text(self, text):
        """
        预处理文本，移除停用词并分词。
        """
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
