from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import *

# Create your views here.

def home(request):
    return HttpResponse('Why not go to <a href="/sources">sources</a>')

def sources(request):
    return HttpResponse("<h2>Sources</h2>" + "<br/>".join([f"<a href='/source/{x.id}'>{str(x)}</a>" for x in Source.objects.all()]))

def source(request, id):
    source_obj = get_object_or_404(Source, pk=id)
    # source_obj = Source.create(name="abaldkjflsadkfj")
    return HttpResponse(f"<h2>{source_obj.name}</h2>")
