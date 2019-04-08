import os

from .crawling_jobs import FuturaSciencesCrawlingJob
from .crawling_jobs import LiberationCrawlingJob
from .crawling_jobs import NouvelObsCrawlingJob
from .crawling_jobs import TeleramaCrawlingJob
from .crawling_jobs import LeFigaroCrawlingJob
from .crawling_jobs import LeMondeCrawlingJob
from .database import Database

from scrapy.utils.log import configure_logging
from scrapy.crawler import CrawlerRunner
from twisted.internet import reactor


class NewspaperCrawler():
    """An autonomous French newspapers crawler.

    Attributes:
        sources_implemented (dict): as keys the newspapers the crawler is able
            to scrap and as values the corresponding CrawlingJob object.
        sources_to_crawl (list): newspapers the crawler has to scrap.
        has_database (boolean): whether or not the crawler has a database.
        db (Database object, optional): allows to interact with the crawler
            database (cf. database module).
    """

    def __init__(self, sources_to_crawl, has_database=False):
        self.sources_implemented = {
                "futurasciences": FuturaSciencesCrawlingJob(has_database),
                "liberation": LiberationCrawlingJob(has_database),
                "nouvelobs": NouvelObsCrawlingJob(has_database),
                "telerama": TeleramaCrawlingJob(has_database),
                "lefigaro": LeFigaroCrawlingJob(has_database),
                "lemonde": LeMondeCrawlingJob(has_database),
                }

        self.sources_to_crawl = set(sources_to_crawl)

        if not self.sources_to_crawl.issubset(self.sources_implemented.keys()):
            out = "Invalid sources_to_crawl: {}\nSources implemented are {}"\
                  .format(self.sources_to_crawl,
                          self.sources_implemented.keys())
            raise ValueError(out)

        self.has_database = has_database
        self._init_storage_instances()

    def _init_storage_instances(self):
        """Checks if storage instances exist, creates them if not.

        By storages instances we mean: a text file storing articles' url
        already met, newspaper directories where to store scrapped
        informations, and finally a SQLite database.
        """
        filename = "urls_met.txt"

        if not os.path.exists(filename):
            with open(filename, "w"): pass

        for source in self.sources_to_crawl:
            directory = "pressarticles/" + source

            if not os.path.exists(directory):
                os.makedirs(directory)

        if self.has_database:
            self.db = Database(db_name="newspaper_db")
        else:
            self.db = None

    def start_crawling(self):
        """Runs newspapers crawling job inside a Twisted reactor.

        See Twisted documentation for more information:
            'http://twistedmatrix.com/documents/current/core/howto/reactor-basics.html'
        """
        configure_logging()
        runner = CrawlerRunner()

        for source in self.sources_to_crawl:
            self.sources_implemented[source].crawl()

        reactor.run()
