from django.shortcuts import render, HttpResponseRedirect
from django_elasticsearch_dsl import Index, Document
from .models import Post, BlogPost, BlogPostIndex
from elasticsearch_dsl import Search

def search(author):
    s = BlogPostIndex.search().query('match', author=author)
    return s


def index(request):

    input = request.POST.get('searchinput')
    print('Input is', input)

    if input:
        posts = search(input)
        print('Output is', list(posts))
    else:
        posts = ''

    return render(request, 'index.html', {'posts': posts})


def add(request):

    #Post.init()
    # create and save and article
    article = BlogPost(title='Mosharrof Rubel', author='rubel', posted_date='2020-04-15', text='Content is about mosharrof rubel')
    article.indexing()

    return HttpResponseRedirect('/')