from django.db import models

class Resource(models.Model):
    """
    Resources RSS
    """
    name = models.CharField(max_length=64)
    url = models.URLField(verify_exists=True)


class Article(models.Model):
    """
    Parsed articles
    """
    title = models.CharField(max_length=1024)
    slug = models.SlugField(max_length=1024)
    url = models.URLField()
    created = models.DateTimeField()
    updated = models.DateTimeField()
    content = models.TextField()

