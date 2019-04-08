from .base_crawling_job import BaseCrawlingJob
from ..spiders import LeFigaroSpider


class LeFigaroCrawlingJob(BaseCrawlingJob):
    
    def __init__(self, has_database):
        BaseCrawlingJob.__init__(self, has_database)
        self.newspaper = "lefigaro"
        self.NewspaperSpider = LeFigaroSpider
        
        self.rss_feeds = [
                "http://www.lefigaro.fr/rss/figaro_actualites-a-la-une.xml",
                "http://www.lefigaro.fr/rss/figaro_politique.xml",
                "http://www.lefigaro.fr/rss/figaro_international.xml",
                "http://www.lefigaro.fr/rss/figaro_actualite-france.xml",
                "http://www.lefigaro.fr/rss/figaro_sciences.xml",
                "http://www.lefigaro.fr/rss/figaro_sante.xml",
                "http://www.lefigaro.fr/rss/figaro_economie.xml",
                "http://www.lefigaro.fr/rss/figaro_societes.xml",
                "http://www.lefigaro.fr/rss/figaro_secteur_high-tech.xml",
                "http://www.lefigaro.fr/rss/figaro_immobilier.xml",
                "http://www.lefigaro.fr/rss/figaro_bourse.xml",
                "http://www.lefigaro.fr/rss/figaro_culture.xml",
                "http://www.lefigaro.fr/rss/figaro_cinema.xml",
                "http://www.lefigaro.fr/rss/figaro_musique.xml",
                "http://www.lefigaro.fr/rss/figaro_livres.xml",
                "http://www.lefigaro.fr/rss/figaro_lifestyle.xml",
                ]
