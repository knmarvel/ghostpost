from django.shortcuts import render
from posts.forms import GhostPostForm


def index(request):
    html = "index.html"
    return render(request, html)