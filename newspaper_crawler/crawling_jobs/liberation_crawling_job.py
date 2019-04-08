from .base_crawling_job import BaseCrawlingJob
from ..spiders import LiberationSpider


class LiberationCrawlingJob(BaseCrawlingJob):
    
    def __init__(self, has_database):
        BaseCrawlingJob.__init__(self, has_database)
        self.newspaper = "liberation"
        self.NewspaperSpider = LiberationSpider
        
        self.rss_feeds = [
                "http://rss.liberation.fr/rss/latest/",
                "http://rss.liberation.fr/rss/58/",
                "http://rss.liberation.fr/rss/44/",
                "http://rss.liberation.fr/rss/60/",
                "http://rss.liberation.fr/rss/10/",
                "http://rss.liberation.fr/rss/11/",
                "http://rss.liberation.fr/rss/12/",
                "http://rss.liberation.fr/rss/14/",
                ]
