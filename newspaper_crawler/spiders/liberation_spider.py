from ..loaders import LiberationLoader
from .base_spider import BaseSpider
from ..items import NewspaperItem


class LiberationSpider(BaseSpider):
    
    dirname = "liberation"
    newspaper = "Liberation"
    name = dirname
    
    def parse(self, response):
        loader = LiberationLoader(item=NewspaperItem(), selector=response)
        
        loader.add_value("newspaper", self.newspaper)
        loader.add_xpath("description", "//h2[@class='article-standfirst read-left-padding']//text()")
        if response.xpath("//time//@datetime").extract_first(default="") != "":
            loader.add_xpath("date", "//time//@datetime")
        loader.add_xpath("author", "//span[@class='author']//span//text()")
        loader.add_xpath("body", "//div[@class='article-body read-left-padding']/*[not(script)][not(img)][not(video)][not(span[@class='author']//a)]//text()")
        
        item = self.load_item(loader, response)
        self.save(newspaper=self.newspaper, item=item)
