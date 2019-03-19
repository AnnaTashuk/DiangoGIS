# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
from gis.models import Articles


def home(request):
    articles = Articles.objects.all()
    context = {
        'articles': articles
    }
    return render(request, 'gis/home.html', context)
    #return render(request, 'gis/home.html')
    # return HttpResponse("Hello world")


def about(request):
    return render(request, 'gis/about.html')