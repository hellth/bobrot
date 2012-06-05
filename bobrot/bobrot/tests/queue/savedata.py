# -*- coding: utf-8 -*-
import datetime
from django.test import TestCase


from bobrot.bobrot.parser.feed import FeedParser
from bobrot.bobrot.queue.job import ArticleParse

from bobrot.bobrot.models import Article

class SaveResultTest(TestCase):

    def test_save_articles(self):
        feed_parser = FeedParser()
        feed_parser.parse('http://www.vysocina-news.cz/rss/')

        project_path = '/tmp/bobrot'

        for feed_article in feed_parser.article_list:
            article_parser = ArticleParse(project_path, feed_article,
                                          feed_parser.feed_meta)
            data = article_parser.call()

            article = Article()
            article.content = data

            self._import_data_to_model(article, feed_article)
            article.save()


        self.assertEquals(len(feed_parser.article_list), Article.objects.count())

    def _import_data_to_model(self, article, parsed_article):
        article.title = parsed_article.title
        article.url = parsed_article.url
        article.created = datetime.datetime.now()
        article.updated = datetime.datetime.now()
