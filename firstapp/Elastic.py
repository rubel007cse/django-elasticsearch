from django.shortcuts import render, HttpResponseRedirect
from django_elasticsearch_dsl import Index, Document
from .models import BlogPost, BlogPostIndex
from elasticsearch_dsl import Search
from elasticsearch_dsl import MultiSearch, Search
from django.http import HttpResponse
import json
from haystack.query import SearchQuerySet


def index(request):


    input = request.POST.get('search_text','Nope')
    print('Input is: ', input)

    #articles = SearchQuerySet().autocomplete(content_auto=input)

    countries = ["Afghanistan", "Albania", "Algeria", "Andorra", "Angola", "Anguilla", "Antigua & Barbuda", "Argentina",
                 "Armenia", "Aruba", "Australia", "Austria", "Azerbaijan", "Bahamas", "Bahrain", "Bangladesh",
                 "Barbados", "Belarus", "Belgium", "Belize", "Benin", "Bermuda", "Bhutan", "Bolivia",
                 "Bosnia & Herzegovina", "Botswana", "Brazil", "British Virgin Islands", "Brunei", "Bulgaria",
                 "Burkina Faso", "Burundi", "Cambodia", "Cameroon", "Canada", "Cape Verde", "Cayman Islands",
                 "Central Arfrican Republic", "Chad", "Chile", "China", "Colombia", "Congo", "Cook Islands",
                 "Costa Rica", "Cote D Ivoire", "Croatia", "Cuba", "Curacao", "Cyprus", "Czech Republic", "Denmark",
                 "Djibouti", "Dominica", "Dominican Republic", "Ecuador", "Egypt", "El Salvador", "Equatorial Guinea",
                 "Eritrea", "Estonia", "Ethiopia", "Falkland Islands", "Faroe Islands", "Fiji", "Finland", "France",
                 "French Polynesia", "French West Indies", "Gabon", "Gambia", "Georgia", "Germany", "Ghana",
                 "Gibraltar", "Greece", "Greenland", "Grenada", "Guam", "Guatemala", "Guernsey", "Guinea",
                 "Guinea Bissau", "Guyana", "Haiti", "Honduras", "Hong Kong", "Hungary", "Iceland", "India",
                 "Indonesia", "Iran", "Iraq", "Ireland", "Isle of Man", "Israel", "Italy", "Jamaica", "Japan", "Jersey",
                 "Jordan", "Kazakhstan", "Kenya", "Kiribati", "Kosovo", "Kuwait", "Kyrgyzstan", "Laos", "Latvia",
                 "Lebanon", "Lesotho", "Liberia", "Libya", "Liechtenstein", "Lithuania", "Luxembourg", "Macau",
                 "Macedonia", "Madagascar", "Malawi", "Malaysia", "Maldives", "Mali", "Malta", "Marshall Islands",
                 "Mauritania", "Mauritius", "Mexico", "Micronesia", "Moldova", "Monaco", "Mongolia", "Montenegro",
                 "Montserrat", "Morocco", "Mozambique", "Myanmar", "Namibia", "Nauro", "Nepal", "Netherlands",
                 "Netherlands Antilles", "New Caledonia", "New Zealand", "Nicaragua", "Niger", "Nigeria", "North Korea",
                 "Norway", "Oman", "Pakistan", "Palau", "Palestine", "Panama", "Papua New Guinea", "Paraguay", "Peru",
                 "Philippines", "Poland", "Portugal", "Puerto Rico", "Qatar", "Reunion", "Romania", "Russia", "Rwanda",
                 "Saint Pierre & Miquelon", "Samoa", "San Marino", "Sao Tome and Principe", "Saudi Arabia", "Senegal",
                 "Serbia", "Seychelles", "Sierra Leone", "Singapore", "Slovakia", "Slovenia", "Solomon Islands",
                 "Somalia", "South Africa", "South Korea", "South Sudan", "Spain", "Sri Lanka", "St Kitts & Nevis",
                 "St Lucia", "St Vincent", "Sudan", "Suriname", "Swaziland", "Sweden", "Switzerland", "Syria", "Taiwan",
                 "Tajikistan", "Tanzania", "Thailand", "Timor L'Este", "Togo", "Tonga", "Trinidad & Tobago", "Tunisia",
                 "Turkey", "Turkmenistan", "Turks & Caicos", "Tuvalu", "Uganda", "Ukraine", "United Arab Emirates",
                 "United Kingdom", "United States of America", "Uruguay", "Uzbekistan", "Vanuatu", "Vatican City",
                 "Venezuela", "Vietnam", "Virgin Islands (US)", "Yemen", "Zambia", "Zimbabwe"]

    # print('Output is', list(articles))
    return render(request, 'index5.html', {'articles': countries})

    # articles = ['Title 1', 'Title 2', 'Article 1', 'Article 2']
    # if input:
    #     for inputs in articles:
    #         print('Array Item', inputs)
    #         if inputs == input:
    #             print('matched!')
    #             return render(request, 'index5.html', {'articles': articles})
    #         else: return render(request, 'index5.html', {'articles': ['Mosharrof', "Mohan", "Moharruf"]})
    # else:
    #     return render(request, 'index5.html', {'articles': ['Mosharrof', "Mohan", "Moharruf"]})













def hays(request):


    posts = SearchQuerySet().autocomplete(content_auto=request.POST.get('searchinput',''))


    return render(request, 'index3.html', {'posts': posts})


def add(request):

    #Post.init()
    # create and save and article
    article = BlogPost(title='Moshq Rubel', author='mohanrubel', posted_date='2020-04-15', text='Content is about mosharrof rubel')
    article.indexing()

    return HttpResponse("Added!")