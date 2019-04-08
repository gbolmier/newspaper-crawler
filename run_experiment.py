from newspaper_crawler import NewspaperCrawler


sources_to_crawl = [
    "futurasciences",
    "lefigaro",
    "lemonde",
    "liberation",
    "nouvelobs",
    "telerama",
]

crawler = NewspaperCrawler(sources_to_crawl, has_database=True)
crawler.start_crawling()
