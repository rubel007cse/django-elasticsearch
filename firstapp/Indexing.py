from elasticsearch_dsl.connections import connections
from elasticsearch.helpers import bulk
from elasticsearch import Elasticsearch
from .models import BlogPost, BlogPostIndex
from django.http import HttpResponse



# Create a connection to ElasticSearch
connections.create_connection()


# Bulk indexing function, run in shell
def bulk_indexing(request):
    BlogPostIndex.init()
    es = Elasticsearch()
    bulk(client=es, actions=(b.indexing() for b in BlogPost.objects.all().iterator()))
    return HttpResponse("Success!")
