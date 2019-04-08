from .base_crawling_job import BaseCrawlingJob
from ..spiders import NouvelObsSpider


class NouvelObsCrawlingJob(BaseCrawlingJob):

    def __init__(self, has_database):
        BaseCrawlingJob.__init__(self, has_database)
        self.newspaper = "nouvelobs"
        self.NewspaperSpider = NouvelObsSpider
        
        self.rss_feeds = [
                "http://tempsreel.nouvelobs.com/rss.xml",
                "http://tempsreel.nouvelobs.com/politique/rss.xml",
                "http://tempsreel.nouvelobs.com/societe/rss.xml",
                "http://tempsreel.nouvelobs.com/monde/rss.xml",
                "http://tempsreel.nouvelobs.com/economie/rss.xml",
                "http://tempsreel.nouvelobs.com/culture/rss.xml",
                "http://o.nouvelobs.com/high-tech/rss.xml",
                "http://tempsreel.nouvelobs.com/education/rss.xml",
                "http://tempsreel.nouvelobs.com/sport/rss.xml",
                "http://tempsreel.nouvelobs.com/rue89/rss.xml",
                "http://tempsreel.nouvelobs.com/rue89/rue89-nos-vies-connectees/rss.xml",
                "http://tempsreel.nouvelobs.com/rue89/rue89-sur-les-reseaux/rss.xml",
                "http://tempsreel.nouvelobs.com/rue89/sur-le-radar/rss.xml",
                ]
