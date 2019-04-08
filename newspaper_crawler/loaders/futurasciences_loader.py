import re

from scrapy.loader.processors import Compose
from scrapy.loader.processors import Join

from .base_loader import BaseLoader


class FuturaSciencesLoader(BaseLoader):

    def clean_date(rawdata):
        return re.search("[0-9]+/[0-9]+/[0-9]+", rawdata).group(0)

    def clean_author(rawdata):
        return re.sub("Par |, Futura", "", rawdata)

    def clean_body(rawdata):
        to_skip_from = [
            "Lien externe ",
            "Liens externes ",
            "Vous avez aimé cet article ? N'hésitez pas à le partager avec",
            "Les brèves de Futura : ",
            "Intéressé par ce que vous venez de lire ? Abonnez-vous",
        ]

        body = rawdata

        for text_to_skip in to_skip_from:
            new_end = body.rfind(text_to_skip)

            if new_end != -1:
                body = body[: new_end]

        to_skip_start = body.rfind("( function () { var vs")
        to_skip_end = body.rfind("s.parentNode.insertBefore(vs, s); })();")

        if (to_skip_start != -1) and (to_skip_end != -1):
            body = body[: to_skip_start] + body[to_skip_end + 39:]

        return body

    date_in = Compose(lambda d: d[0], clean_date)
    author_out = Compose(Join(", "), clean_author)
    body_out = Compose(Join(" "), clean_body)
