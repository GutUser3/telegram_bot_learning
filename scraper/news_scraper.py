from parsel import Selector
import requests


class NewsScraper:
    PLUS_URL = 'https://kg.akipress.org'
    URL = "https://kg.akipress.org/?from=portal&place=menu"
    LINK_XPATH = '//div[@class="elem"]/div[@class="title"]/a/@href'
    TITLE_XPATH = '//div[@class="elem"]/div[@class="title"]/a/text()'

    def parse_data(self):
        html = requests.get(url=self.URL).text
        tree = Selector(text=html)
        links = tree.xpath(self.LINK_XPATH).extract()
        titles = tree.xpath(self.TITLE_XPATH).extract()
        # for link in links:
        #     print(link)
        # for title in titles:
        #     print(title)
        return links[:5]


if __name__ == "__main__":
    scraper = NewsScraper()
    scraper.parse_data()