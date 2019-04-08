import scrapy


class NewspaperItem(scrapy.Item):
    """Defines fields we want to store for each article.

    See Scrapy documentation for more information:
        'http://docs.scrapy.org/en/latest/topics/items.html'
    """
    url = scrapy.Field()
    newspaper = scrapy.Field()
    theme = scrapy.Field()
    title = scrapy.Field()
    description = scrapy.Field()
    date = scrapy.Field()
    author = scrapy.Field()
    body = scrapy.Field()
