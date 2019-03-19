# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from gis.models import Articles


def home(request):
    articles = Articles.objects.all()
    context = {
        'articles': articles
    }
    return render(request, 'gis/home.html', context)
    # return render(request, 'gis/home.html')
    # return HttpResponse("Hello world")

def show_articles(request, article_id):
    article = get_object_or_404(Articles, id=article_id)
    return render(request, 'gis/article.html', {'article': article})


def about(request):
    return render(request, 'gis/about.html')


def mymap(request):
    return render(request, 'gis/map.html')