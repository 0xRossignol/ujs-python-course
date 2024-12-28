import jieba
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt


class Analyzer:
    url_prefix = "../data/processed/"

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
        return words

    def calculate_word_frequency(self, words):
        """
        统计词频。
        """
        return Counter(words)

    def generate_wordcloud(self, word_freq, output_path=None):
        """
        根据词频生成词云图。
        """
        wc = WordCloud(font_path='msyh.ttc',  # 指定字体路径，确保支持中文
                       width=800, height=400, background_color='white')
        wc.generate_from_frequencies(word_freq)

        # 显示词云
        plt.figure(figsize=(10, 5))
        plt.imshow(wc, interpolation="bilinear")
        plt.axis("off")
        plt.show()

        # 保存词云到文件
        if output_path:
            wc.to_file(Analyzer.url_prefix + output_path)


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

        analyzer.generate_wordcloud(word_freq, output_path="wordcloud.png")
    else:
        print("No articles found for analysis.")
