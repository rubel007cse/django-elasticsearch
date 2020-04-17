from elasticsearch_dsl import connections
from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search
from elasticsearch_dsl.query import MultiMatch, Match
from elasticsearch_dsl import Q, A
from django.shortcuts import render, HttpResponseRedirect, redirect
from .models import BlogPostIndex

# Making the connection
connections.create_connection(hosts=['localhost'], timeout=20)

client = Elasticsearch()


def experiment(request):

    inputs = '2'
    search = Search(index='blogpost-index-v4')

    print('total indexed search sugges', search.filter('match', title_suggest=inputs).count())

    query = search.suggest(
        'title-suggestions',
        inputs,
        completion={
        'field': 'title_suggest',
        'fuzzy': True
        })

    s = query.execute()
    print('hola', s.to_dict())

    return render(request, 'index2.html', {'response': s, 'inputs': inputs})

