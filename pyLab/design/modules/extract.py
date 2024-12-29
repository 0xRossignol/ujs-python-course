class Extract:
    CONTENT = 1
    TITLE = 2
    URL = 3

    def content(self, articles):
        with open("../data/extract/content.txt", 'w', encoding='utf-8') as fp:
            for article in articles:
                text = article.get('content')
                if text:
                    fp.write(text + '\n')

    def title(self, articles):
        with open("../data/extract/title.txt", 'w', encoding='utf-8') as fp:
            for article in articles:
                text = article.get('title')
                if text:
                    fp.write(text + '\n')

    def url(self, articles):
        with open("../data/extract/url.txt", 'w', encoding='utf-8') as fp:
            for article in articles:
                text = article.get('url')
                if text:
                    fp.write(text + '\n')


if __name__ == "__main__":
    extract = Extract()
    articles = [
        {"title": "Elon Musk’s xAI lands $6B in new cash", "url": "https://techcrunch.com/article1"},
        {"title": "TechCrunch Disrupt 2024 Recap", "url": "https://techcrunch.com/article2"},
        {"content": 'goByExample pt.2'},
        {"content": 'Go by Example: Functions'},
        {"content": 'Functions are central (核心/中心) in Go. We’ll learn about functions with a few different examples.'},
        {"content": 'Here’s a function that takes two ints and returns their sum as an int'},
        {"content": 'Go requires explicit returns,i.e. (即 )it won’t automatically return the value of the last expression.'}
    ]

    extract.content(articles)
