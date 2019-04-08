import re

from scrapy.loader.processors import Compose
from scrapy.loader.processors import Join

from .base_loader import BaseLoader


class LiberationLoader(BaseLoader):
    
    def clean_date(rawdata):
        date = re.sub("[^0-9-]", "", rawdata)
        date = date[0:len(date)-6]
        date = date.replace("-", "/")
        date = date.split("/")
        date[2], date[0] = date[0], date[2]
        date = "/".join(date)
        return date

    def clean_title(rawdata):
        return rawdata[0].replace(" - Libération", "")
    
    def clean_author(rawdata):
        return rawdata.replace(" LIBERATION", "")

    date_in = Compose(lambda v: v[0], clean_date)
    title_in = Compose(clean_title)
    author_out = Compose(Join(", "), clean_author)
