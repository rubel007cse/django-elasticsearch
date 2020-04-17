import elasticsearch_dsl as es
from django_elasticsearch_dsl import Document, Index
from django.db import models
from django.utils import timezone
from elasticsearch_dsl import Document, Text, Date, Search, Completion



# ElasticSearch "model" mapping out what fields to index
class BlogPostIndex(Document):
    author = Text()
    posted_date = Date()
    title = Text()
    text = Text()

    class Index:
        name = 'blogpost-index-v4'

# Blogpost to be indexed into ElasticSearch
class BlogPost(models.Model):
    author = models.CharField(max_length=200)
    posted_date = models.DateField(default=timezone.now)
    title = models.CharField(max_length=200)
    text = models.TextField(max_length=1000)

    # Method for indexing the model
    def indexing(self):
        obj = BlogPostIndex(
            meta={'id': self.id},
            author=self.author,
            posted_date=self.posted_date,
            title=self.title,
            text=self.text
        )
        obj.save()
        return obj.to_dict(include_meta=True)




class Article(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    pub_date = models.DateField(default=timezone.now)

    def __unicode__(self):
        return self.title
