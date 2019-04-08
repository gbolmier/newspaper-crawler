from .base_crawling_job import BaseCrawlingJob
from ..spiders import FuturaSciencesSpider


class FuturaSciencesCrawlingJob(BaseCrawlingJob):
    
    def __init__(self, has_database):
        BaseCrawlingJob.__init__(self, has_database)
        self.newspaper = "futura-sciences"
        self.NewspaperSpider = FuturaSciencesSpider
        
        self.rss_feeds = [
                "http://www.futura-sciences.com/rss/actualites.xml",
                "http://www.futura-sciences.com/rss/sante/actualites.xml",
                "http://www.futura-sciences.com/rss/high-tech/actualites.xml",
                "http://www.futura-sciences.com/rss/espace/actualites.xml",
                "http://www.futura-sciences.com/rss/environnement/actualites.xml",
                "http://www.futura-sciences.com/rss/maison/actualites.xml",
                "http://www.futura-sciences.com/rss/nature/actualites.xml",
                "http://www.futura-sciences.com/rss/terre/actualites.xml",
                "http://www.futura-sciences.com/rss/matiere/actualites.xml",
                "http://www.futura-sciences.com/rss/mathematiques/actualites.xml",
                ]
