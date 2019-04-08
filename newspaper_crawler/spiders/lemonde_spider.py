from ..loaders import LeMondeLoader
from .base_spider import BaseSpider
from ..items import NewspaperItem


class LeMondeSpider(BaseSpider):

    dirname = "lemonde"
    newspaper = "Le Monde"
    name = dirname

    def parse(self, response):
        loader = LeMondeLoader(item=NewspaperItem(), selector=response)

        loader.add_value("newspaper", self.newspaper)
        loader.add_xpath("description", "//p[@class='article__desc']//text()")
        if response.xpath("//meta[@property='og:article:published_time']/@content").extract_first(default="") != "":
            loader.add_xpath("date", "//meta[@property='og:article:published_time']/@content")
        loader.add_xpath("author", "//span[@class='meta__author']//text()")
        loader.add_xpath("body", "//section[@class='article__content  old__article-content-single']//p//text()")

        item = self.load_item(loader, response)
        self.save(newspaper=self.newspaper, item=item)
