import requests
from bs4 import BeautifulSoup
import time
import random


class Crawler:
    def __init__(self, headers=None, proxies=None):
        # 随机 user_agents 以实现反爬
        self.user_agents = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
            "(KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",

            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
            "(KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36",

            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
            "(KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",

            "Mozilla/5.0 (iPhone; CPU iPhone OS 14_5_1 like Mac OS X)"
            " AppleWebKit/605.1.15 "
            "(KHTML, like Gecko) Version/14.1 Mobile/15E148 Safari/604.1"
        ]
        self.headers = headers if headers else {}
        self.proxies = proxies if proxies else []

    def fetch_html(self, url):
        """
        Fetches the HTML content of the given URL with random User-Agent and optional proxy.
        """
        try:
            # 随机选择 User-Agent
            self.headers["User-Agent"] = random.choice(self.user_agents)

            # 随机选择代理（如果有代理可用）
            proxy = random.choice(self.proxies) if self.proxies else None
            proxy_dict = {"http": proxy, "https": proxy} if proxy else None

            print(f"Fetching {url} with User-Agent: {self.headers['User-Agent']} Proxy: {proxy}")

            response = requests.get(url, headers=self.headers, proxies=proxy_dict, timeout=10)
            response.raise_for_status()

            # 随机延迟，模拟正常用户行为
            time.sleep(random.uniform(1, 3))

            return response.text
        except requests.RequestException as e:
            print(f"Error fetching {url}: {e}")
            return None

    def parse_html(self, html):
        """
        处理爬取到的内容
        """
        try:
            soup = BeautifulSoup(html, 'html.parser')
            articles = soup.find_all(['a', 'p'])
            results = []

            for article in articles:
                # 如果是<a>标签且包含href属性，才获取链接
                if article.name == 'a' and article.has_attr('href'):
                    results.append({
                        "title": article.get_text(strip=False),
                        "url": article['href']
                    })
                # 如果是<p>标签，则只获取标题文本
                elif article.name == 'p':
                    results.append({
                        "title": None,
                        "content": article.get_text(strip=False),
                        "url": None
                    })

            return results
        except Exception as e:
            print(f"Error parsing HTML: {e}")
            return None


if __name__ == "__main__":
    url = "https://www.zhihu.com/"
    """
    使用代理反爬：
        如果目标网站对单个 IP 地址有访问限制，可以配置 HTTP 或 HTTPS 代理。
    """
    # proxies = [
    #
    # ]
    crawler = Crawler()

    html = crawler.fetch_html(url)
    if html:
        articles = crawler.parse_html(html)
        if articles:
            print("Extracted Articles:")
            for i, article in enumerate(articles, start=1):
                print(f"{i}. {article['title']} - {article['url']}")
        else:
            print("No articles found.")
