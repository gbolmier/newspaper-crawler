from ..loaders import FuturaSciencesLoader
from .base_spider import BaseSpider
from ..items import NewspaperItem


class FuturaSciencesSpider(BaseSpider):
    
    dirname = "futurasciences"
    newspaper = "Futura Sciences"
    name = dirname
    
    def parse(self, response):
        loader = FuturaSciencesLoader(item=NewspaperItem(), selector=response)
        
        loader.add_value("newspaper", self.newspaper)
        loader.add_xpath("description", "//p[@class='delta py0p5']//text()")
        if response.xpath("//time//text()").extract_first(default="") != "":
            loader.add_xpath("date", "//time//text()")
        loader.add_xpath("author", "//h3[@itemprop='author']//text()")
        loader.add_xpath("body", "//section[@class='module article-text article-text-classic bg-white']/*[not(script)][not(img)][not(video)]//text()")
        
        item = self.load_item(loader, response)
        self.save(newspaper=self.newspaper, item=item)
