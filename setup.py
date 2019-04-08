from setuptools import find_packages
from setuptools import setup

import newspaper_crawler


setup(
    author="Geoffrey Bolmier",
    author_email="geoffrey.bolmier@gmail.com",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.6",
        "Topic :: Scientific/Engineering",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    description="An autonomous French newspaper crawler based on Scrapy framework",
    install_requires=[
        "feedparser>=5.2.1",
        "scrapy>=1.5.1",
    ],
    license="MIT",
    name="newspaper-crawler",
    packages=find_packages(),
    python_requires=">=3.6.5",
    url="http://github.com/gbolmier/newspaper-crawler",
    version=newspaper_crawler.__version__,
)
