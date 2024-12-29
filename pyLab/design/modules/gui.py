import tkinter as tk
from tkinter import messagebox
from tkinter import scrolledtext
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

from design.modules.analyzer import Analyzer
from design.modules.crawler import Crawler
from design.modules.storage import DataSaver
from design.modules.visualize import Visualizer
from design.modules.extract import Extract
from design.modules.search import Search
from design.modules.ai import AiSummary


class WebCrawlerGUI:
    # 初始化模块
    saver = DataSaver(db_name="articles.db", file_name="articles.txt", excel_name="articles.xlsx")
    analyzer = Analyzer(stopwords=Analyzer.stop_words)
    visualizer = Visualizer()
    extract = Extract()
    search = Search()
    ai = AiSummary()
    text = None
    articles = None

    # 可视化所需数据
    top_10, keys, values, wordcloud_data = None, None, None, None

    # 下拉框选项
    options = ["Wiki", "Google", "百度", "Bing"]

    def __init__(self, root):
        self.root = root
        self.root.title("Web Crawler")
        self.root.geometry("800x500")

        self.base_url = tk.StringVar()
        self.word = tk.StringVar()

        # 输入网址框
        self.url_label = ttk.Label(root, text="请输入 URL:",
                                   font=("SimSun", 10))
        self.url_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.url_entry = ttk.Entry(root,
                                   textvariable=self.base_url,
                                   width=50,
                                   bootstyle=DARK)
        self.url_entry.grid(row=0, column=1, padx=10, pady=5)

        # 爬取按钮
        self.crawl_button = ttk.Button(root, text="开始爬取",
                                       command=lambda: {
                                           self.start_crawl(),
                                           self.start_analyze()
                                       },
                                       bootstyle="dark-outline")
        self.crawl_button.grid(row=0, column=2, columnspan=1, pady=10,)

        # 显示爬取结果的文本框
        self.result_text = scrolledtext.ScrolledText(root, width=90, height=15, wrap=tk.WORD,
                                                     font=("SimSun", 10))
        self.result_text.grid(row=3, column=0, columnspan=3, pady=10)

        # 保存模块按钮
        self.save_button_db = ttk.Button(root, text="以数据库保存",
                                         command=lambda: self.save_results(mode=DataSaver.DB_MODE),
                                         bootstyle="dark-outline")
        self.save_button_db.grid(row=4, column=0, padx=0, pady=10)

        self.save_button_text = ttk.Button(root, text="以text保存",
                                           command=lambda: self.save_results(mode=DataSaver.TEXT_MODE),
                                           bootstyle="dark-outline")
        self.save_button_text.grid(row=4, column=1, padx=0, pady=10)

        self.save_button_excel = ttk.Button(root, text="以excel保存",
                                            command=lambda: self.save_results(mode=DataSaver.EXCEL_MODE),
                                            bootstyle="dark-outline")
        self.save_button_excel.grid(row=4, column=2, padx=0, pady=10)

        # 可视化模块按钮
        self.visualize_button_bar = ttk.Button(root, text="显示为柱状图",
                                               command=lambda: self.visualize_opts(mode=Visualizer.BAR_CHARTS),
                                               bootstyle="dark-outline")
        self.visualize_button_bar.grid(row=5, column=0, padx=0, pady=10)

        self.visualize_button_pie = ttk.Button(root, text="显示为饼状图",
                                               command=lambda: self.visualize_opts(mode=Visualizer.PIE_CHARTS),
                                               bootstyle="dark-outline")
        self.visualize_button_pie.grid(row=5, column=1, padx=0, pady=10)

        self.visualize_button_wc = ttk.Button(root, text="显示为词云图",
                                              command=lambda: self.visualize_opts(mode=Visualizer.WORDCLOUD),
                                              bootstyle="dark-outline")
        self.visualize_button_wc.grid(row=5, column=2, padx=0, pady=10)

        # 提取模块按钮
        self.content_button = ttk.Button(root, text="仅输出内容",
                                         command=lambda: self.start_extract(mode=Extract.CONTENT),
                                         bootstyle="dark-outline")
        self.content_button.grid(row=2, column=0, padx=0, pady=10)

        self.title_button = ttk.Button(root, text="仅输出标题",
                                       command=lambda: self.start_extract(mode=Extract.TITLE),
                                       bootstyle="dark-outline")
        self.title_button.grid(row=2, column=1, padx=0, pady=10)

        self.url_button = ttk.Button(root, text="仅输出url",
                                     command=lambda: self.start_extract(mode=Extract.URL),
                                     bootstyle="dark-outline")
        self.url_button.grid(row=2, column=2, padx=0, pady=10)

        self.url_button = ttk.Button(root, text="输出ai概括",
                                     command=lambda: self.start_summary(),
                                     bootstyle="dark-outline")
        self.url_button.grid(row=0, column=3, padx=0, pady=10)

        # 搜索模块
        # 输入网址框
        self.search_label = ttk.Label(root, text="请输入想搜索的词:", font=("SimSun", 10))
        self.search_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.search_entry = ttk.Entry(root, textvariable=self.word, width=50, bootstyle=DARK)
        self.search_entry.grid(row=1, column=1, padx=10, pady=5)

        # 创建下拉框
        self.combo_box = ttk.Combobox(root, values=self.options, state="readonly", bootstyle=DARK)  # 设置为只读模式
        self.combo_box.grid(row=1, column=2, padx=10, pady=5)
        self.combo_box.set("请选择使用的搜索引擎")  # 设置初始显示值

        # 搜索按钮
        self.search_button = ttk.Button(root, text="搜索",
                                        command=lambda: {
                                            self.start_search()
                                        },
                                        bootstyle="dark-outline")
        self.search_button.grid(row=1, column=3, columnspan=2, pady=10)

    def start_crawl(self):
        url = self.base_url.get().strip()
        if not url:
            messagebox.showwarning("Input Error", "请输入正确的URL")
            return

        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, f"Crawling {url}...\n")

        # 爬取内容
        crawler = Crawler()
        html = crawler.fetch_html(url)
        articles = crawler.parse_html(html)

        if not articles:
            messagebox.showerror("Error", "爬取失败")
            return

        self.result_text.insert(tk.END, f"Found {len(articles)} articles:\n")
        for article in articles:
            if article.get("title"):
                self.result_text.insert(tk.END, f"{article['title']} - {article['url']}\n")
            elif article.get("content"):
                self.result_text.insert(tk.END, f"{article['content']}\n")

        self.text = " ".join(
            (article.get('title') or article.get('content', '')).strip()
            for article in articles if article.get('title') or article.get('content')
        )
        # 保存内容
        self.articles = articles

    def start_analyze(self):
        if not  self.articles:
            return

        # 词汇分析
        words = self.analyzer.preprocess_text(self.text)
        word_freq = self.analyzer.calculate_word_frequency(words)
        print("Word Frequency:", word_freq.most_common(10))  # 显示前10高频词

        # 获取前 10 个高频词（返回的是一个列表，元素是 (key, value) 元组）
        self.wordcloud_data = [(word, freq) for word, freq in word_freq.items()]
        self.top_10 = word_freq.most_common(10)
        self.keys = [item[0] for item in self.top_10]
        self.values = [item[1] for item in self.top_10]

    def save_results(self, mode=DataSaver.DB_MODE):
        if not ((self.keys and self.values) and self.top_10 and self.wordcloud_data and self.articles):
            messagebox.showwarning("Error", "请先爬取相应网站内容")
            return

        if mode is None:
            pass
        if mode == DataSaver.DB_MODE:
            self.saver.save_to_db(self.articles)
        if mode == DataSaver.TEXT_MODE:
            self.saver.save_to_text(self.articles)
        if mode == DataSaver.EXCEL_MODE:
            self.saver.save_to_excel(self.articles)

        messagebox.showinfo("Save Successful", "数据保存成功！")

    def visualize_opts(self, mode=None):
        if not ((self.keys and self.values) and self.top_10 and self.wordcloud_data):
            messagebox.showwarning("Error", "请先爬取相应网站内容")
            return

        if mode is None:
            pass
        if mode == self.visualizer.BAR_CHARTS:
            self.visualizer.generate_bar_chart(self.keys, self.values, "BAR_CHARTS")
        if mode == self.visualizer.PIE_CHARTS:
            self.visualizer.generate_pie_chart(self.top_10, "PIE_CHARTS")
        if mode == self.visualizer.WORDCLOUD:
            self.visualizer.generate_wordcloud(self.wordcloud_data, "WORDCLOUD")

    def start_extract(self, mode=None):
        if not ((self.keys and self.values) and self.top_10 and self.wordcloud_data and self.articles):
            messagebox.showwarning("Error", "请先爬取相应网站内容")
            return

        if mode is None:
            pass
        if mode == self.extract.CONTENT:
            self.extract.content(self.articles)
        if mode == self.extract.TITLE:
            self.extract.title(self.articles)
        if mode == self.extract.URL:
            self.extract.url(self.articles)

        messagebox.showinfo("extract Successful", "数据提取成功！")

    def start_search(self):
        select_item = self.combo_box.get()
        word = self.word.get()
        if not word:
            messagebox.showwarning("Input Error", "请输入单词")
            return

        if select_item is None:
            pass
        if select_item == self.search.WIKI:
            self.search.go_to_wiki(word)
        if select_item == self.search.GOOGLE:
            self.search.go_to_google(word)
        if select_item == self.search.BAIDU:
            self.search.go_to_baidu(word)
        if select_item == self.search.BING:
            self.search.go_to_bing(word)

        # messagebox.showinfo("search Successful", f"成功跳转到{select_item}: {word}")

    def start_summary(self):
        if not ((self.keys and self.values) and self.top_10 and self.wordcloud_data and self.articles):
            messagebox.showwarning("Error", "请先爬取相应网站内容")
            return

        messagebox.showinfo("start summary", "正在概括，请稍等。。。")

        self.result_text.delete(1.0, tk.END)

        self.extract.content(self.articles)
        summary = self.ai.summary()

        self.result_text.insert(tk.END, summary)


# 启动GUI应用
if __name__ == "__main__":
    root = tk.Tk()
    gui = WebCrawlerGUI(root)
    root.mainloop()
