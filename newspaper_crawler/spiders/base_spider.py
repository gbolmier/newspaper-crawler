import unicodedata
import scrapy
import json
import abc

from datetime import datetime


class BaseSpider(scrapy.Spider, abc.ABC):
    """Base spider, defines how to scrape a newspaper website.

    See Scrapy documentation for more information:
        'https://docs.scrapy.org/en/latest/topics/spiders.html'

    Attributes:
        dirname (string): directory name where the articles (jsons) are stored.
        newspaper (string): name of the scraped newspaper.
        db: (Database object, optional): allows to interact with the crawler
            database (cf. database module).
        start_urls (list): urls to crawl.
        custom_settings (dict): configuration when running the spider.
        article_count (int): number of articles scraped by the instance.
    """

    custom_settings = {"DOWNLOAD_DELAY": 2}
    article_count = 0

    @abc.abstractmethod
    def parse(self, response):
        """Parses an article before processing and saving it.

        Args:
            response (scrapy Response object): the http response of the scraped
                web page.
        """

    def load_item(self, loader, response):
        """Extracts and processes informations from an article.

        Args:
            loader (scrapy Loader object): able to scrape data from a response.
            response (scrapy Response object): the http response of the scraped
                web page.

        Returns:
            item (scrapy Item object): populated with scraped and processed
                data.
        """
        loader.add_value("title", response.css("title::text").extract_first())
        loader.add_value("theme", response.url)
        loader.add_value("url", response.url)
        item = loader.load_item()

        return item

    def save(self, newspaper, item):
        """Saves scraped data into json files and in database if asked.

        Args:
            newspaper (string): name of the newspaper.
            item (scrapy Item object): populated with scraped and processed
                data.
        """
        missing_keys = list(set(item.fields.keys()) - set(item.keys()))

        for missing_key in missing_keys:
            item[missing_key] = ""

        if len(item["body"]) > 2100:

            if item["date"] == "":
                time = datetime.now()
                item["date"] = "{}/{}/{}".format(time.day, time.month,
                                                 time.year)

            self.article_count += 1
            filename = "{} #{}.json".format(newspaper, self.article_count)
            filepath = "pressarticles/{}/{}".format(self.dirname, filename)

            with open(filepath, "w", encoding="utf-8") as f:
                json.dump(dict(item), f, indent=4)
                self.log("Saved file {}".format(filename))

            if self.db != None:
                self.db.insert_article(
                    url=item["url"],
                    source=newspaper,
                    author=item["author"],
                    title=item["title"],
                    theme=item["theme"],
                    description=item["description"],
                    date_published=item["date"],
                    body=item['body'],
                )
