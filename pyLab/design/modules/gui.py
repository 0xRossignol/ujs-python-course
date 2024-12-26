import tkinter as tk
from tkinter import messagebox
from tkinter import scrolledtext

from design.modules.analyzer import Analyzer
from design.modules.crawler import Crawler
from design.modules.storage import DataSaver


class WebCrawlerGUI:
    articles = None

    def __init__(self, root):
        self.root = root
        self.root.title("Web Crawler")
        self.root.geometry("600x500")

        self.base_url = tk.StringVar()

        # 输入网址框
        self.url_label = tk.Label(root, text="Enter website URL:")
        self.url_label.pack(pady=10)
        self.url_entry = tk.Entry(root, textvariable=self.base_url, width=50)
        self.url_entry.pack(pady=5)

        # 爬取按钮
        self.crawl_button = tk.Button(root, text="Crawl Website", command=self.start_crawl)
        self.crawl_button.pack(pady=10)

        # 显示爬取结果的文本框
        self.result_text = scrolledtext.ScrolledText(root, width=70, height=15, wrap=tk.WORD)
        self.result_text.pack(pady=10)

        # 保存按钮
        self.save_button = tk.Button(root, text="Save Results", command=self.save_results)
        self.save_button.pack(pady=10)

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

        # Step 2: Analyze word frequency
        text = " ".join(article['title'] for article in articles)

        # 初始化分析器
        stopwords = {"的", "在", "了", "是", "和", "也", "与", "等", "to", "the", "of", "How"}  # 可扩展停用词
        analyzer = Analyzer(stopwords=stopwords)

        # 词汇分析和生成词云
        words = analyzer.preprocess_text(text)
        word_freq = analyzer.calculate_word_frequency(words)
        print("Word Frequency:", word_freq.most_common(10))  # 显示前10高频词

        analyzer.generate_wordcloud(word_freq, output_path="wordcloud.png")

        # Save the articles to disk
        self.articles = articles

    def save_results(self):
        if not hasattr(self, 'articles'):
            messagebox.showwarning("Save Error", "No data to save!")
            return

        saver = DataSaver(db_name="articles.db", file_name="articles.txt", excel_name="articles.xlsx")
        saver.save_to_db(self.articles)
        saver.save_to_text(self.articles)
        saver.save_to_excel(self.articles)
        messagebox.showinfo("Save Successful", "Data saved successfully!")


# 启动GUI应用
if __name__ == "__main__":
    root = tk.Tk()
    gui = WebCrawlerGUI(root)
    root.mainloop()
