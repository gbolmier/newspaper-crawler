from scrapy.loader.processors import Compose
from scrapy.loader.processors import Join

from .base_loader import BaseLoader


class LeMondeLoader(BaseLoader):

    def clean_date(rawdata):
        return rawdata[: 10]

    def clean_author(rawdata):
        return rawdata.replace(" Par  ", "")

    def clean_description(rawdata):
        return rawdata[2: -1]

    date_in = Compose(lambda v: v[0], clean_date)
    author_out = Compose(Join(", "), clean_author)
    description_out = Compose(Join(", "), clean_description)
