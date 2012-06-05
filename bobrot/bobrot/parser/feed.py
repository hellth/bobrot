# coding: utf-8
'''
    Všechny hodnoty které se berou z RSS musí mít bloky try a catch, protože každý kanál je nevyspytatelný, může
    totiž mít např. jiné kódování souborů než uvádí, různé formáty času atd.
'''
import re

import feedparser
import time

from bobrot.bobrot.parser.sanitizer import Sanitizer

class Article(object):

    """
    V papirove dokumentaci tomu Volda rika APIArticle
    Uchovava veskere data tykajici se clanku vcetne obsahu,
    pri stahovani html by mohl obsahovat i html.
    Je treba doresit jak se bude webscammer ucit
    """
    def __init__(self, title, summary, url, created):
        self.title = unicode(title)
        self.summary = unicode(summary)
        self.url = str(url)
        self.created = created
        self.text = ''
        self.density = 0.0

    @property
    def created_as_string(self):
        return time.strftime('%Y-%m-%d--%H-%M-%S', self.created)

class FeedMeta(object):

    def __init__(self, domain, site, created, language, encode):
        self.domain = domain
        self.site = site
        self.created = created
        self.language = language
        self.encode = encode

    @property
    def created_as_string(self):
        return time.strftime('%Y-%m-%d', self.created)

class FeedParser(object):

    def parse(self, feed_url):
        feed = self.get_feed_list(feed_url)

        self.feed_meta = self.generete_meta_information(feed)
        self.article_list = self.parse_article_list(feed)


    def generete_meta_information(self, feed):
        encode = feed['encoding'] if len(feed['encoding']) > 0 else ''

        language = self._get_language(feed)

        domain = re.match(r'^http://([a-zA-Z0-9\.-]*)',
                          feed['feed']['link']).group(1)
        site = re.match(r'^http://([a-zA-Z0-9\.-]*)',
                        feed['feed']['links'][0]['href']).group(1)
        created = feed['feed']['updated_parsed']

        return FeedMeta(domain, site, created, language, encode)

    def parse_article_list(self, feed):
        article_list = []
        for article in feed['entries']:
            article_list.append(self.parse_article(article))

        return article_list


    def parse_article(self, article):
        sanitizer = Sanitizer()

        title = sanitizer.replace_bad_characters(article['title'])
        summary = sanitizer.replace_bad_characters(article['summary'])
        url = article['links'][0]['href']
        time_created_article = article['updated_parsed']

        return Article(title, summary, url, time_created_article)

    def _get_language(self, feed):
        self.language = feed['feed']['language'] if len(
            self._sanitize_language(feed['feed']['language'])) > 0 else ''

    def _sanitize_language(self, lang):
        sanitizer = Sanitizer()
        return sanitizer.replace_bad_characters(lang)

    def get_feed_list(self, feed_url):
        return feedparser.parse(feed_url)

