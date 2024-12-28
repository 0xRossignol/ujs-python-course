from pyecharts import options as opts
from pyecharts.charts import Pie
from pyecharts.charts import Bar
import webbrowser
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from design.modules.analyzer import Analyzer


class Visualizer:
    url_prefix = ("file:///C:/Users/Rossignol/Desktop/school/courses/"
                  "python/python-school/pyLab/design/data/visualizations/")
    name_prefix = "../data/visualizations/"
    BAR_CHARTS = 1
    PIE_CHARTS = 2
    WORDCLOUD_MODE = 3

    def generate_bar_chart(self, x_data, y_data, filename):
        fullname = self.name_prefix + filename + ".html"
        path = self.url_prefix + filename + ".html"
        # 创建柱状图
        bar = Bar()
        bar.add_xaxis(x_data)
        bar.add_yaxis("单词出现数", y_data)

        # 配置图表
        bar.set_global_opts(
            title_opts=opts.TitleOpts(title="菜鸟教程技术出现数柱状图"),
            xaxis_opts=opts.AxisOpts(name="名称"),
            yaxis_opts=opts.AxisOpts(name="出现数"),
        )

        # 渲染图表
        bar.render(fullname)

        # 查看图表
        webbrowser.open(path)

    def generate_pie_chart(self, data, filename):
        fullname = self.name_prefix + filename + ".html"
        path = self.url_prefix + filename + ".html"
        # 创建饼状图
        pie = Pie()
        pie.add("", data)

        # 配置图表
        pie.set_global_opts(
            title_opts=opts.TitleOpts(title="菜鸟教程技术出现数饼状图"),
            legend_opts=opts.LegendOpts(pos_bottom='0')
        )

        # 渲染图表
        pie.render(fullname)

        # 查看图表
        webbrowser.open(path)

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
        stopwords = {"的", "在", "了", "是", "和", "也", "与", "等",
                     "教程", "学习", "一个", "一种", "免费", "一套"}  # 可扩展停用词
        analyzer = Analyzer(stopwords=stopwords)
        test = Visualizer()

        # Step 3: 词汇分析和生成词云
        words = analyzer.preprocess_text(text)
        word_freq = analyzer.calculate_word_frequency(words)
        print("Word Frequency:", word_freq.most_common(10))  # 显示前10高频词

        # 获取前 10 个高频词（返回的是一个列表，元素是 (key, value) 元组）
        top_10 = word_freq.most_common(10)
        keys = [item[0] for item in top_10]
        values = [item[1] for item in top_10]
        print(keys)
        print(values)
        test.generate_wordcloud(word_freq, output_path="wordcloud.png")
        test.generate_bar_chart(keys, values, "test1")
        test.generate_pie_chart(top_10, "test2")
    else:
        print("No articles found for analysis.")

