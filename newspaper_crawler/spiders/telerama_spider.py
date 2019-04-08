from ..loaders import TeleramaLoader
from .base_spider import BaseSpider
from ..items import NewspaperItem


class TeleramaSpider(BaseSpider):

    dirname = "telerama"
    newspaper = "Telerama"
    name = dirname

    def parse(self, response):
        loader = TeleramaLoader(item=NewspaperItem(), selector=response)

        loader.add_value("newspaper", self.newspaper)
        loader.add_xpath("description", "//div[@class='article--intro']//p//text()")
        if response.xpath("//span[@itemprop='datePublished']//text()").extract_first(default="") != "":
            loader.add_xpath("date", "//span[@itemprop='datePublished']//text()")
        if response.xpath("//div[@class='article--meta']//li//text()").extract_first(default="") != "":
            loader.add_xpath("author", "//div[@class='article--meta']//li//text()")
        elif response.xpath("//div[@class='article--meta']//img//@alt").extract_first(default="") != "":
            loader.add_xpath("author", "//div[@class='article--meta']//img//@alt")
        loader.add_xpath("body", "//div[@class='article--wysiwyg wysiwyg ']/*[not(script)][not(img)][not(video)]//text()")

        item = self.load_item(loader, response)
        self.save(newspaper=self.newspaper, item=item)
