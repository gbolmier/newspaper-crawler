from ..loaders import NouvelObsLoader
from .base_spider import BaseSpider
from ..items import NewspaperItem


class NouvelObsSpider(BaseSpider):

    dirname = "nouvelobs"
    newspaper = "Nouvel Obs"
    name = dirname

    def parse(self, response):
        loader = NouvelObsLoader(item=NewspaperItem(), selector=response)

        loader.add_value("newspaper", self.newspaper)
        loader.add_xpath("description", "//div[@class='ObsArticle-chapo full']//h2//text()")
        if response.xpath("//time//a//@href").extract_first(default="") != "":
            loader.add_xpath("date", "//time//a//@href")
        loader.add_xpath("author", "//div[@class='ObsArticle-author full']//span//text()")
        loader.add_xpath("body", "////div[@id='ObsArticle-body']/*[not(script)][not(img)][not(video)]//text()")

        item = self.load_item(loader, response)
        self.save(newspaper=self.newspaper, item=item)
