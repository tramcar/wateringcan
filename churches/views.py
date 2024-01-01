#from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import Page


def index(request):
    page = get_object_or_404(Page, pk=1)
    return render(request, "churches/index.html", {"page": page})


def detail(request, page_id):
    page = get_object_or_404(Page, pk=page_id)
    return render(request, "churches/detail.html", {"page": page})


def detail_slug(request, page_slug):
    page = get_object_or_404(Page, slug=page_slug)
    return render(request, "churches/detail.html", {"page": page})