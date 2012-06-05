# coding: utf-8
import datetime
from bobrot.bobrot.parser.feed import Article as ApiArticle, FeedParser
from bobrot.bobrot.models import Article, Resource
from bobrot.bobrot.queue.job import ArticleParse

def get_parsed_articles():
    article_list = []
    for resource in Resource.objects.all():
        feed_parser = FeedParser()
        feed_parser.parse(resource.url)

        project_path = '/tmp/bobrot'


        for feed_article in feed_parser.article_list:
            article = ArticleParse(project_path, feed_article,
                feed_parser.feed_meta)

            article_list.append(article.get_api_article())

    return article_list


def save_api_article_list(article_list):
    now = datetime.datetime.now()
    for api_article in article_list:
        assert isinstance(api_article, ApiArticle)

        article = Article()
        article.title = api_article.title
        article.url = api_article.url
        article.created = now
        article.updated = now
        article.save()
