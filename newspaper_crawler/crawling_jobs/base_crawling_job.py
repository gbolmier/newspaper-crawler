import feedparser

from scrapy.crawler import CrawlerRunner
from twisted.internet import reactor

from ..database import Database


class BaseCrawlingJob():
    """Base class for newspaper crawling process.
    
    Attributes:
        has_database (boolean): whether or not the crawler has a database.
        db (Database object, optional): allows to interact with the crawler
            database (cf. database module).
        newspaper (string): name of the scraped newspaper.
        NewspaperSpider (Class inheriting from scrapy.Spider): defines how to
            scrape the newspaper.
        rss_feeds (list): rss urls where to find newspaper new articles.
    """
    
    def __init__(self, has_database):
        self.has_database = has_database
        if self.has_database:
            self.db = Database(db_name="newspaper_db")
        else:
            self.db = None
        
    def crawl(self, delay=3600):
        """Crawls newspaper articles not crawled yet every `x` seconds.
        
        Args:
            delay (int): delay in seconds before next crawling job.
                   Defaults to 1 hour.
        """
        urls_to_crawl = self.get_urls_to_crawl()
        
        if len(urls_to_crawl) > 0:
            runner = CrawlerRunner()
            runner.crawl(self.NewspaperSpider, start_urls=urls_to_crawl,
                         db=self.db)
        
        reactor.callLater(delay, self.crawl)
    
    def get_urls_to_crawl(self):
        """Returns a list of the newspaper urls not crawled yet."""
        urls = []
        
        for rss_feed in self.rss_feeds:
            parsed_rss_feed = feedparser.parse(rss_feed)
            
            for post in parsed_rss_feed.entries:
                url = post.link
                
                if url.split(".")[1] == self.newspaper:
                    with open("urls_met.txt", "r") as f:
                        urls_met = f.read().split("\n")
                        
                    if url not in urls_met:
                        entry = "\n{}".format(url)

                        with open("urls_met.txt", "a", encoding="utf-8") as f:
                            f.write(entry)
                            
                        urls.append(url)
                        
        return urls
