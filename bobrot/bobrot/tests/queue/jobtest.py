# -*- coding: utf-8 -*-
import time
from unittest import TestCase
import os

from bobrot.bobrot.parser.feed import FeedMeta, Article
from bobrot.bobrot.queue.job import ArticleParse



class ArticleParseTest(TestCase):

    def setUp(self):
        self.feed_meta = FeedMeta('nwoo.org/rss.php', 'nwoo.org/rss.php',
                             time.localtime(), 'cs', 'utf-8')
        self.article = Article('Foo', 'Description',
                          'http://www.nwoo.org/view.php?cisloclanku=2012040100', time.localtime())

        self.project_path = '/tmp/bobrot'


    def test_build_args(self):

        expected = [
            'wget',
            '%s' % self.article.url,
            '-O %s' % '/'.join([
                self.project_path, self.feed_meta.domain,
                self.feed_meta.created_as_string,
                '/html/'
                '%s.html' % self.article.title
                ]),
            ' --convert-links'
        ]
        feed = ArticleParse(self.project_path, self.article, self.feed_meta)
        self.assertEquals(expected, feed.build_args())

    def test_call(self):
        feed = ArticleParse(self.project_path, self.article, self.feed_meta)
        feed.call()

        self.assertTrue(os.path.exists(feed.get_filename()))