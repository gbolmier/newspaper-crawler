# :spider: Newspaper crawler

This repository hosts a French newspaper crawler based on [`Scrapy`](http://scrapy.org/) framework.

The web crawler crawls the target sources every hours for new articles (time step parameter can be tuned). Scraped articles are stored individually in `json` files and optionally in a `sqlite` database.

Stored article example:

```json
{
    "newspaper": "Futura Sciences",
    "date": "05/04/2019",
    "author": "Fabrice Auclert",
    "theme": "tech",
    "title": "L’IA d’IBM peut vous dire quand vous allez démissionner !",
    "description": "En interne, IBM utilise l'intelligence artificielle pour anticiper les départs de ses employés. Selon sa P.-D.G., le taux de réussite est de 95 % !",
    "url": "https://www.futura-sciences.com/tech/actualites/intelligence-artificielle-ia-ibm-peut-vous-dire-vous-allez-demissionner-75624/",
    "body": "En interne, IBM utilise l'intelligence artificielle pour anticiper les départs de ses employés. Selon sa P.-D.G., le taux de réussite est de 95 % ! L' intelligence artificielle  va permettre de créer des milliers d'emplois à travers le monde, mais elle pourrait aussi se transformer en DRH du futur. C'est ce qu'a expliqué Ginni Rometty, la P.-D.G. d' IBM . En marge d'une conférence sur le travail et les ressources humaines à New York, elle a expliqué que  IBM  avait développé une  application  pour anticiper les départs de ses collaborateurs, et ainsi mieux les retenir. Avec 350.000 employés à travers le monde, et une forte concurrence sur le marché des technologies, IBM ne veut pas voir partir ses meilleurs éléments, et l'IA sert à fidéliser ses employés. «  Le meilleur moment pour récupérer un employé, c'est avant son départ  », a-t-elle expliqué et c'est pour cette raison que sa firme a déposé un brevet  sur un « programme de calcul du départ prédictif ». C'est évidemment lié à  Watson , et Ginny Rometty avance un taux de réussite de 95 %. Forcément, elle ne veut pas dévoiler le secret de son application mais de multiples et divers paramètres entrent en jeu tels que l'âge de l'employé(e), l'expérience, ou encore le salaire, l'ancienneté dans l'entreprise et la  durée  des trajets au quotidien pour se rendre au bureau.    Le département des ressources humaines réduit de 30 % Cet outil vient en complément des avis de la direction des Ressources humaines, mais IBM reconnaît avoir considérablement limité ses effectifs dans ce secteur car il est basé sur un modèle aujourd'hui dépassé. «  Les humains ont besoin de l'IA pour améliorer leur travail  » affirme la dirigeante d'IBM, qui révèle que son département des ressources humaines a été réduit de 30 %. Ceux qui restent sont alors mieux payés, et ils profitent de l' IA  pour mieux identifier les compétences des collaborateurs et mieux les guider sur un plan de carrière. L'assistant virtuel AI MYCA ( My Career Advisor ) d'IBM utilise ainsi Watson pour aider les employés à identifier les domaines dans lesquels ils ont besoin d'améliorer leurs compétences. En complément, la technologie  Blue Match  leur offre des possibilités d'emploi en fonction des données compilées et extraites par l'IA. La P.-D.G. affirme que plus d'un quart des employés d'IBM qui ont reçu un nouvel emploi ou une promotion en 2018 ont été assistés par Blue Match. La P.-D.G. d'IBM estime que l'IA permet de mieux identifier les compétences des employés, mais aussi leurs limites. © CNBC, Youtube À l'inverse, l' intelligence artificielle  permet aussi de mieux cibler les compétences inutiles. «  Si vous possédez une compétence qui n'est pas nécessaire pour l'avenir, qui est abondante sur le marché et qui ne correspond pas à la stratégie visée par mon entreprise, vous ne pouvez pas rester à l'intérieur  », n'hésite pas à expliquer Ginny Rometty, ajoutant que l'IA possède un immense avantage par rapport à l'humain, l'objectivité : «  Les responsables sont subjectifs dans les évaluations. Nous pouvons trancher et être plus précis à partir des données . » En vigueur chez IBM, ces solutions sont mises à la disposition de n'importe quelle entreprise. Ce qu'il faut retenir Pour épauler la direction des Ressources humaines, IBM fait appel à l'intelligence artificielle. Pour anticiper les volontés de départ ou orienter des employés, l'IA s'appuie sur des données objectives. Utilisé en interne, ce programme affiche un taux de réussite de 95 %."
}
```

6 sources have been implemented: [Le Monde](http://www.lemonde.fr), [Le Figaro](http://www.lefigaro.fr), [Libération](http://www.liberation.fr), [Futura-Sciences](http://www.futura-sciences.com), [Le Nouvel Obs](http://www.nouvelobs.com) and [Télérama](http://www.telerama.fr).

Crawling scheme consists of repeating:
1) Get new articles from RSS feeds
2) Scrape and save them
3) Wait an hour

## Installation

Run `pip install git+https://github.com/gbolmier/newspaper-crawler` in a terminal.

If you want to install `newspaper-crawler` module in a specific conda environment beware of using the [corresponding local `pip`](https://github.com/ContinuumIO/anaconda-issues/issues/1429).

## Quick example

[run_experiment.py](run_experiment.py) script:

```python
>>> from newspaper_crawler import NewspaperCrawler

>>> sources_to_crawl = [
...         "futurasciences",
...         "lefigaro",
...         "lemonde",
...         "liberation",
...         "nouvelobs",
...         "telerama",
...         ]

>>> crawler = NewspaperCrawler(sources_to_crawl, has_database=True)
>>> crawler.start_crawling()
```

## Miscellaneous

Project architecture:

```
└───newspaper_crawler
    │   __init__.py
    │   crawler.py
    │   database.py
    │   items.py
    │
    ├───crawling_jobs
    │       __init__.py
    │       base_crawling_job.py
    │       futurasciences_crawling_job.py
    │       lefigaro_crawling_job.py
    │       lemonde_crawling_job.py
    │       liberation_crawling_job.py
    │       nouvelobs_crawling_job.py
    │       telerama_crawling_job.py
    │
    ├───loaders
    │       __init__.py
    │       base_loader.py
    │       futurasciences_loader.py
    │       lefigaro_loader.py
    │       lemonde_loader.py
    │       liberation_loader.py
    │       nouvelobs_loader.py
    │       telerama_loader.py
    │
    └───spiders
            __init__.py
            base_spider.py
            futurasciences_spider.py
            lefigaro_spider.py
            lemonde_spider.py
            liberation_spider.py
            nouvelobs_spider.py
            telerama_spider.py
```

Right after being launched, 3 storage instances are created in the crawler script directory:
- `newspaper_db` sqlite file containing each scraped articles (database is optional)
- `urls_met.txt` storing each url found in the rss feeds to avoid scraping the same article multiple times
- `pressarticles` directory with a subdirectory by scraped source, each one storing a json file by scraped article

Storage instances:

```
│   newspaper_db
│   urls_met.txt
│
└───pressarticles
    ├───futurasciences
    │       Futura Sciences #1.json
    │       Futura Sciences #2.json
    │       Futura Sciences #3.json
    |       ...
    │
    ├───lefigaro
    │       Le Figaro #1.json
    │       ...
    │
    ├───lemonde
    │       Le Monde #1.json
    │       ...
    │
    ├───liberation
    │       Liberation #1.json
    │       ...
    │
    ├───nouvelobs
    │       Nouvel Obs #1.json
    │       ...
    │
    └───telerama
            Telerama #1.json
            ...
```

## License

MIT license, [see here](LICENSE).
