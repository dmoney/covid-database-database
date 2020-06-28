from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import *

import markdown

# Create your views here.

def home(request):
    return render(request, 'home.html')

def sources(request):
    return render(request, 'sources.html', {"sources": Source.objects.all()})

def source(request, id):
    source_obj = get_object_or_404(Source, pk=id)
    using = source_obj.using.all()
    used_by = source_obj.used_by.all()

    # cuz who needs functions when we can instantiate a class
    # to then call a method upon...
    md = markdown.Markdown()
    description_html = md.convert(source_obj.description)

    return render(request, 'source.html', {
        "source": source_obj,
        "description_html": description_html,
        "using_sources": using,
        "used_by_sources": used_by,
        })
