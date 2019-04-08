from scrapy.loader.processors import Compose, TakeFirst

from .base_loader import BaseLoader


class TeleramaLoader(BaseLoader):

    def clean_date(rawdata):
        date = rawdata[len(rawdata)-11:len(rawdata)]
        date = date.replace(".", "")
        return date

    def clean_title(rawdata):
        title = rawdata[0].replace(" - Télérama.fr", "")
        position = title.rfind(" -")
        title = title[0:position]
        return title

    date_in = Compose(lambda v: v[0], clean_date)
    title_in = Compose(clean_title)
    author_out = TakeFirst()
