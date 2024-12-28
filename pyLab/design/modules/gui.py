import tkinter as tk
from tkinter import messagebox
from tkinter import scrolledtext

from design.modules.analyzer import Analyzer
from design.modules.crawler import Crawler
from design.modules.storage import DataSaver
from design.modules.visualize import Visualizer


class WebCrawlerGUI:
    # 初始化模块
    saver = DataSaver(db_name="articles.db", file_name="articles.txt", excel_name="articles.xlsx")
    visualizer = Visualizer()

    text = None
    articles = None
    '''
    以下是可视化所需数据
    '''
    top_10, keys, values, wordcloud_data = None, None, None, None

    def __init__(self, root):
        self.root = root
        self.root.title("Web Crawler")
        self.root.geometry("750x500")

        self.base_url = tk.StringVar()

        # 输入网址框
        self.url_label = tk.Label(root, text="Enter website URL:")
        self.url_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.url_entry = tk.Entry(root, textvariable=self.base_url, width=50)
        self.url_entry.grid(row=0, column=1, padx=10, pady=5)

        # 爬取按钮
        self.crawl_button = tk.Button(root, text="Crawl Website",
                                      command=lambda: {
                                          self.start_crawl(),
                                          self.start_analyze()
                                      })
        self.crawl_button.grid(row=1, column=0, columnspan=2, pady=10)

        # 显示爬取结果的文本框
        self.result_text = scrolledtext.ScrolledText(root, width=70, height=15, wrap=tk.WORD)
        self.result_text.grid(row=2, column=0, columnspan=2, pady=10)

        '''
        保存模块
        '''
        # 保存模块按钮
        self.save_button_db = tk.Button(root, text="Save Results To DB",
                                        command=lambda: self.save_results(mode=DataSaver.DB_MODE))
        self.save_button_db.grid(row=3, column=0, padx=0, pady=10)

        self.save_button_text = tk.Button(root, text="Save Results To text",
                                          command=lambda: self.save_results(mode=DataSaver.TEXT_MODE))
        self.save_button_text.grid(row=3, column=1, padx=0, pady=10)

        self.save_button_excel = tk.Button(root, text="Save Results To excel",
                                           command=lambda: self.save_results(mode=DataSaver.EXCEL_MODE))
        self.save_button_excel.grid(row=3, column=2, padx=0, pady=10)

        '''
        可视化模块
        '''
        # 可视化模块按钮
        self.visualize_button_bar = tk.Button(root, text="Bar Charts",
                                              command=lambda: self.visualize_opts(mode=Visualizer.BAR_CHARTS))
        self.visualize_button_bar.grid(row=4, column=0, padx=0, pady=10)

        self.visualize_button_pie = tk.Button(root, text="Pie Charts",
                                              command=lambda: self.visualize_opts(mode=Visualizer.PIE_CHARTS))
        self.visualize_button_pie.grid(row=4, column=1, padx=0, pady=10)

        self.visualize_button_wc = tk.Button(root, text="WordCloud",
                                             command=lambda: self.visualize_opts(mode=Visualizer.WORDCLOUD))
        self.visualize_button_wc.grid(row=4, column=2, padx=0, pady=10)

    def start_crawl(self):
        url = self.base_url.get().strip()
        if not url:
            messagebox.showwarning("Input Error", "Please enter a valid URL")
            return

        self.result_text.delete(1.0, tk.END)  # Clear the text box
        self.result_text.insert(tk.END, f"Crawling {url}...\n")

        # Step 1: Crawl articles
        crawler = Crawler()
        html = crawler.fetch_html(url)
        articles = crawler.parse_html(html)

        if not articles:
            messagebox.showerror("Error", "Failed to retrieve articles")
            return

        self.result_text.insert(tk.END, f"Found {len(articles)} articles:\n")
        for article in articles:
            self.result_text.insert(tk.END, f"{article['title']} - {article['url']}\n")

        self.text = " ".join(article['title'] for article in articles)
        # Save the articles to disk
        self.articles = articles

    def start_analyze(self):
        # 初始化分析器

        analyzer = Analyzer(stopwords=Analyzer.stop_words)

        # 词汇分析和生成词云
        words = analyzer.preprocess_text(self.text)
        word_freq = analyzer.calculate_word_frequency(words)
        print("Word Frequency:", word_freq.most_common(10))  # 显示前10高频词

        # 获取前 10 个高频词（返回的是一个列表，元素是 (key, value) 元组）
        self.wordcloud_data = [(word, freq) for word, freq in word_freq.items()]
        self.top_10 = word_freq.most_common(10)
        self.keys = [item[0] for item in self.top_10]
        self.values = [item[1] for item in self.top_10]

    def save_results(self, mode=DataSaver.DB_MODE):
        if not hasattr(self, 'articles'):
            messagebox.showwarning("Save Error", "No data to save!")
            return

        if mode is None:
            pass
        if mode == DataSaver.DB_MODE:
            self.saver.save_to_db(self.articles)
        if mode == DataSaver.TEXT_MODE:
            self.saver.save_to_text(self.articles)
        if mode == DataSaver.EXCEL_MODE:
            self.saver.save_to_excel(self.articles)

        messagebox.showinfo("Save Successful", "Data saved successfully!")

    def visualize_opts(self, mode=None):
        if not hasattr(self, 'articles'):
            messagebox.showwarning("Error", "No data to visualize!")
            return

        if mode is None:
            pass
        if mode == self.visualizer.BAR_CHARTS:
            self.visualizer.generate_bar_chart(self.keys, self.values, "BAR_CHARTS")
        if mode == self.visualizer.PIE_CHARTS:
            self.visualizer.generate_pie_chart(self.top_10, "PIE_CHARTS")
        if mode == self.visualizer.WORDCLOUD:
            self.visualizer.generate_wordcloud(self.wordcloud_data, "WORDCLOUD")


# 启动GUI应用
if __name__ == "__main__":
    root = tk.Tk()
    gui = WebCrawlerGUI(root)
    root.mainloop()
