from django.shortcuts import render
from django.http import HttpResponse
from datetime import date
from app.models import Donut

def index(request):
    donuts = Donut.objects.all()

    return render(request, 'index.html', {
       'donuts': donuts,
    })

def donut(request, id):
    d = Donut.objects.get(pk=id)
    context = {'donut': d}

    return render(request, 'donut.html', context)