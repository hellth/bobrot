# coding: utf-8
import time

from unittest import TestCase

from bobrot.bobrot.parser.feed import FeedParser, FeedMeta, Article

class FeedParserTest(TestCase):

    def test_parse(self):
        """
        Tohle je opravdu dummy test, jestli se z parseru dostane to co ma.
        Chce to jeste osetrovat a testovat jeho funkcionalitu.
        """
        parser = FeedParser()
        parser.parse('http://nwoo.org/rss.php')

        self.assertIsInstance(parser.feed_meta, FeedMeta)
        [self.assertIsInstance(article, Article) for article in parser.article_list]

