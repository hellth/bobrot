# coding: utf-8
__author__ = 'hellth'
from subprocess import call
from random import randint
from BeautifulSoup import BeautifulStoneSoup
import os
import re
import unicodedata
import feedparser
import pprint

# Trida dostane jeden rss kanal a vsechny jeho zaznamy/clanky a ty zpracovava/porovnava
#
# Default path 'Date_string/domain/%H/
class Bobrot(self, rsschan):
    def __init__(self, rsschan):
        self.rsschan = rsschan

    # Load articles from RSS to list, return list of values
    #
    # Article header = 'string'
    # Slug = 'string' # name-of-file = replace_bad_chracters(article)
    # Url = 'string'
    # Date = date # feeds entries updated_parsed
    # Date_update = date # feed entries updated
    # Date_string = 'string' #YYYY-mm-dd
    # Date_hour = 'string'
    # Date_min = 'string'
    # Date_sec = 'string'
    # Text = 'string'
    # Html = 'string'
    # Compared = list[]
    # Compared_articles = list[]
    # Compared_articles_relevancy = 0
    # Compared_articles_diff = 'string' #diff string
    #
    # words_relevancy = int
    # words_diffusion = int # rozptyl slov, kolik slov je brano za relevantni text / soucast mnoziny
    # words_diffusion_range = int # jaky rozptyl je bran jako mnozina
    # words_diffusion_vector = # jaky venktor zaindexovaneho slova - vyskyt slova v clanku

    def get_articles(self):
        pass

    # Compare articles and return diff/relevancy
    def compare_articles(self,articles):
        pass

    # Search for areas with words / returns relevancy
    def search_words(self,article):
        pass

    # Save object to database - article in plaintext
    def save(self):
        pass
