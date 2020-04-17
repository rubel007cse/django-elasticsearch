from elasticsearch_dsl import connections
from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search
from elasticsearch_dsl.query import MultiMatch, Match
from elasticsearch_dsl import Q, A
from django.shortcuts import render, HttpResponseRedirect, redirect
from .models import BlogPostIndex

# Making the connection
connections.create_connection(hosts=['localhost'], timeout=20)




def experiment(request):

    client = Elasticsearch()
    response = client.search(
        index="blogpost-index-v4",
        body={
                "query": {
                    "fuzzy": {
                        "title": {
                            "value": "blayer"
                        }
                    }
                }
            }
    )



    return render(request, 'index2.html', {'response': response, 'inputs': ''})

