from elasticsearch_dsl.connections import connections
from elasticsearch.helpers import bulk
from elasticsearch import Elasticsearch
from .models import BlogPost, BlogPostIndex
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create a connection to ElasticSearch
connections.create_connection()


# Bulk indexing function, run in shell
def bulk_indexing():
    BlogPostIndex.init()
    es = Elasticsearch()
    bulk(client=es, actions=(b.indexing() for b in BlogPost.objects.all().iterator()))
