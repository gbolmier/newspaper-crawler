from scrapy.loader.processors import TakeFirst
from scrapy.loader.processors import Compose
from scrapy.loader.processors import Join
from scrapy.loader import ItemLoader


class BaseLoader(ItemLoader):
    """Base loader for processing scrapped data.
    
    See Scrapy documentation for more information:
        'http://docs.scrapy.org/en/latest/topics/loaders.html'
    """
    
    def clean_theme(rawdata):
        theme = str(rawdata).split("/")
        theme = theme[3]
        theme = theme.replace("-", " ")
        return theme
    
    theme_in = Compose(clean_theme)
    default_output_processor = TakeFirst()
    author_out = Join(", ")
    body_out = Join(" ")
