from django.shortcuts import render, HttpResponseRedirect
from django_elasticsearch_dsl import Index, Document
from .models import BlogPost, BlogPostIndex
from elasticsearch_dsl import Search
from elasticsearch_dsl import MultiSearch, Search
from django.http import HttpResponse
import json
from haystack.query import SearchQuerySet
from elasticsearch import Elasticsearch
import random, json

client = Elasticsearch()


def index(request):

    return render(request, 'index5.html', {'alldata': [] })







def searchdata(request):

    input = request.POST.get('search_text','None')
    print('Input is: ', input)


    response = client.search(
        index="blogpost-index-v4",
        body={
                "query": {
                    "match_phrase_prefix": {
                            "title": {
                                    "query": input,
                                    "slop": 10
                        }
                    }
                }
            }
    )


    alldata =response['hits']['hits']


    bloodytitles = []

    for data in alldata:
        bloodytitles.append(data['_source']['title'])


    print('Output Array is: ', bloodytitles)

    finaldata = {}
    finaldata['status'] = 'success'
    finaldata['alladata'] = bloodytitles

    return HttpResponse(json.dumps(finaldata), content_type="application/json")











def hays(request):


    posts = SearchQuerySet().autocomplete(content_auto=request.POST.get('searchinput',''))


    return render(request, 'index3.html', {'posts': posts})


def add(request):

    #Post.init()
    # create and save and article
    article = BlogPost(title='blayer bush', author='blayerbhai bush', posted_date='2020-04-15', text='Amaderbush blayerbhai2')
    article.indexing()

    return HttpResponse("Added!")