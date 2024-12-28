import sqlite3
import pandas as pd


class DataSaver:
    url_prefix = "../data/raw/"

    DB_MODE = 1
    TEXT_MODE = 2
    EXCEL_MODE = 3

    def __init__(self, db_name="words.db", file_name="words.txt", excel_name="words.xlsx"):
        self.db_name = DataSaver.url_prefix + db_name
        self.file_name = DataSaver.url_prefix + file_name
        self.excel_name = DataSaver.url_prefix + excel_name

    def save_to_db(self, articles):
        """
        Saves articles to an SQLite database.
        """
        try:
            connection = sqlite3.connect(self.db_name)
            cursor = connection.cursor()

            # Create table if it doesn't exist
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS articles (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    url TEXT NOT NULL
                )
            """)

            # Insert articles into the table
            cursor.executemany("""
                INSERT INTO articles (title, url) VALUES (?, ?)
            """, [(article['title'], article['url']) for article in articles])

            connection.commit()
            print(f"Saved {len(articles)} articles to the database: {self.db_name}")
        except Exception as e:
            print(f"Error saving to database: {e}")
        finally:
            connection.close()

    def save_to_text(self, articles):
        """
        Saves articles to a plain text file.
        """
        try:
            with open(self.file_name, 'w', encoding='utf-8') as file:
                for article in articles:
                    file.write(f"Title: {article['title']}\nURL: {article['url']}\n\n")
            print(f"Saved {len(articles)} articles to text file: {self.file_name}")
        except Exception as e:
            print(f"Error saving to text file: {e}")

    def save_to_excel(self, articles):
        """
        Saves articles to an Excel file.
        """
        try:
            df = pd.DataFrame(articles)
            df.to_excel(self.excel_name, index=False, engine='openpyxl')
            print(f"Saved {len(articles)} articles to Excel file: {self.excel_name}")
        except Exception as e:
            print(f"Error saving to Excel: {e}")


# 示例代码
if __name__ == "__main__":
    # 示例文章列表
    articles = [
        {"title": "Elon Musk’s xAI lands $6B in new cash", "url": "https://techcrunch.com/article1"},
        {"title": "TechCrunch Disrupt 2024 Recap", "url": "https://techcrunch.com/article2"}
    ]

    # 初始化 DataSaver 对象
    saver = DataSaver()

    # 保存到 SQLite 数据库
    saver.save_to_db(articles)

    # 保存到文本文件
    saver.save_to_text(articles)

    # 保存到 Excel 文件
    saver.save_to_excel(articles)
