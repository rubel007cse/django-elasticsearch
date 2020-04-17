"""elasticdjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from firstapp.Elastic import index,add, hays
from firstapp.ElasticV2 import experiment
from firstapp.Indexing import bulk_indexing


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, ),
    path('hays', hays, ),
    path('add', add, ),
    path('bulk_indexing', bulk_indexing, ),
    path('experiment', experiment, name='experiment'),
    path('cars/', include('cars.urls', namespace='cars')),
    path('search/', include('haystack.urls'))
]
