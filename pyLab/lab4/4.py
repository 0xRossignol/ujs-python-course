import requests
from bs4 import BeautifulSoup
import threading
import tkinter as tk
from tkinter import messagebox


# 定义爬取网页的函数
def crawl(url, result_text, status_label):
    try:
        # 修改状态
        status_label.config(text="正在爬取数据...", fg="blue")

        # 发送请求
        response = requests.get(url)
        response.raise_for_status()  # 如果返回状态码不是 200，则抛出异常
        html_content = response.text

        # 使用 BeautifulSoup 解析网页内容
        soup = BeautifulSoup(html_content, 'html.parser')
        text_content = soup.get_text()  # 获取网页中的文本部分

        # 保存爬取到的数据到本地文件
        with open("output.txt", "w", encoding="utf-8") as file:
            file.write(text_content)

        # 在界面上显示爬取到的数据
        result_text.delete(1.0, tk.END)  # 清空之前的内容
        result_text.insert(tk.END, text_content)  # 插入新内容

        # 更新状态
        status_label.config(text="爬取完成", fg="green")
        messagebox.showinfo("信息", "爬取成功！数据已保存到 output.txt 文件中。")

    except requests.RequestException as e:
        status_label.config(text="爬取失败", fg="red")
        messagebox.showerror("错误", f"请求失败: {e}")
    except Exception as e:
        status_label.config(text="发生错误", fg="red")
        messagebox.showerror("错误", f"发生错误: {e}")


# 启动爬虫的线程函数
def start_crawl_thread(url, result_text, status_label):
    # 创建一个新线程来爬取数据，避免阻塞界面
    crawl_thread = threading.Thread(target=crawl, args=(url, result_text, status_label))
    crawl_thread.start()


# 创建 GUI 界面
def create_gui():
    # 初始化窗口
    window = tk.Tk()
    window.title("简单爬虫")
    window.geometry("600x400")

    # URL 输入框
    url_label = tk.Label(window, text="请输入网址:")
    url_label.pack(pady=10)
    example_label = tk.Label(window, text="例如：http://baidu.com")
    example_label.pack(pady=10)
    url_entry = tk.Entry(window, width=50)
    url_entry.pack(pady=10)

    # 显示爬取结果的文本框
    result_text = tk.Text(window, width=80, height=10, wrap=tk.WORD)
    result_text.pack(pady=10)

    # 爬虫状态标签
    status_label = tk.Label(window, text="准备开始爬取", fg="black")
    status_label.pack(pady=10)

    # 爬取按钮
    crawl_button = tk.Button(window, text="开始爬取",
                             command=lambda: start_crawl_thread(url_entry.get(), result_text, status_label))
    crawl_button.pack(pady=20)

    # 启动 GUI 窗口的主循环
    window.mainloop()


# 主函数
if __name__ == "__main__":
    create_gui()
