import re

from scrapy.loader.processors import Compose
from scrapy.loader.processors import Join

from .base_loader import BaseLoader


class LeFigaroLoader(BaseLoader):

    def clean_date(rawdata):
        return re.search("[0-9]+/[0-9]+/[0-9]+", rawdata).group(0)

    def clean_author(rawdata):
        author = rawdata.replace("lefigaro.fr", "")
        return re.search("\w+[\w ]+", author).group(0)

    date_in = Compose(lambda v: v[0], clean_date)
    author_out = Compose(Join(", "), clean_author)
