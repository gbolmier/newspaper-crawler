from .base_crawling_job import BaseCrawlingJob
from ..spiders import LeMondeSpider


class LeMondeCrawlingJob(BaseCrawlingJob):
    
    def __init__(self, has_database):
        BaseCrawlingJob.__init__(self, has_database)
        self.newspaper = "lemonde"
        self.NewspaperSpider = LeMondeSpider
        
        self.rss_feeds = [
                "http://www.lemonde.fr/rss/une.xml",
                "http://www.lemonde.fr/international/rss_full.xml",
                "http://www.lemonde.fr/politique/rss_full.xml",
                "http://www.lemonde.fr/les-decodeurs/rss_full.xml",
                "http://www.lemonde.fr/societe/rss_full.xml",
                "http://www.lemonde.fr/m-actu/rss_full.xml",
                "http://www.lemonde.fr/football/rss_full.xml",
                "http://www.lemonde.fr/afrique/rss_full.xml",
                "http://www.lemonde.fr/ameriques/rss_full.xml",
                "http://www.lemonde.fr/argent/rss_full.xml",
                "http://www.lemonde.fr/asie-pacifique/rss_full.xml",
                "http://www.lemonde.fr/culture/rss_full.xml",
                "http://www.lemonde.fr/emploi/rss_full.xml",
                "http://www.lemonde.fr/europe/rss_full.xml",
                "http://www.lemonde.fr/idees/rss_full.xml",
                "http://www.lemonde.fr/jeux-video/rss_full.xml",
                "http://www.lemonde.fr/pixels/rss_full.xml",
                "http://www.lemonde.fr/planete/rss_full.xml"
                "http://www.lemonde.fr/proche-orient/rss_full.xml",
                "http://www.lemonde.fr/sante/rss_full.xml",
                "http://www.lemonde.fr/sciences/rss_full.xml",
                "http://www.lemonde.fr/sport/rss_full.xml",
                "http://www.lemonde.fr/m-styles/rss_full.xml",
                ]
