import webbrowser


class Search:
    wiki_url_prefix = 'https://zh.wikipedia.org/wiki/'
    google_url_prefix = 'https://www.google.com/search?q='
    baidu_url_prefix = 'https://www.baidu.com/s?wd='
    bing_url_prefix = 'https://www.bing.com/search?q='

    WIKI = "Wiki"
    GOOGLE = "Google"
    BAIDU = "百度"
    BING = "Bing"

    def go_to_wiki(self, word: str):
        webbrowser.open(self.wiki_url_prefix + word)

    def go_to_google(self, word: str):
        webbrowser.open(self.google_url_prefix + word)

    def go_to_baidu(self, word: str):
        webbrowser.open(self.baidu_url_prefix + word)

    def go_to_bing(self, word: str):
        webbrowser.open(self.bing_url_prefix + word)


if __name__ == "__main__":

    wiki_fetcher = Search()
    # wiki_fetcher.go_to_wiki("go")
    wiki_fetcher.go_to_google("go")
