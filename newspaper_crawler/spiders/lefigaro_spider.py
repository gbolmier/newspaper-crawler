from ..loaders import LeFigaroLoader
from .base_spider import BaseSpider
from ..items import NewspaperItem


class LeFigaroSpider(BaseSpider):

    dirname = "lefigaro"
    newspaper = "Le Figaro"
    name = dirname

    def parse(self, response):
        loader = LeFigaroLoader(item=NewspaperItem(), selector=response)

        loader.add_value("newspaper", "Le Figaro")
        loader.add_xpath("description", "//p[@class='fig-content__chapo']//text()")
        if response.xpath("//time//text()").extract_first(default="") != "":
            loader.add_xpath("date", "//time//text()")
        loader.add_xpath("author", "//a[@class='fig-content-metas__author']//text()")
        loader.add_xpath("body", "//div[@class='fig-content__body']/*[not(script)][not(img)][not(video)]//text()")

        item = self.load_item(loader, response)
        self.save(newspaper=self.newspaper, item=item)
