from .base_crawling_job import BaseCrawlingJob
from ..spiders import TeleramaSpider


class TeleramaCrawlingJob(BaseCrawlingJob):
    
    def __init__(self, has_database):
        BaseCrawlingJob.__init__(self, has_database)
        self.newspaper = "telerama"
        self.NewspaperSpider = TeleramaSpider
        
        self.rss_feeds = [
                "http://www.telerama.fr/rss/une.xml",
                "http://www.telerama.fr/rss/medias.xml",
                "http://www.telerama.fr/rss/television.xml",
                "http://www.telerama.fr/rss/radio.xml",
                "http://www.telerama.fr/rss/cinema.xml",
                "http://www.telerama.fr/rss/series-tv.xml",
                "http://www.telerama.fr/rss/musique.xml",
                "http://www.telerama.fr/rss/livre.xml",
                "http://www.telerama.fr/rss/scenes.xml",
                "http://www.telerama.fr/rss/services/cinema.xml",
                "http://www.telerama.fr/rss/services/disque.xml",
                "http://www.telerama.fr/rss/services/livre.xml",
                "http://www.telerama.fr/rss/services/art.xml",
                ]
