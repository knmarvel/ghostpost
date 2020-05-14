from django.shortcuts import render
from posts.forms import GhostPostForm
from posts.models import GhostPost
from posts.helpers import public_url_maker, private_url_maker


def index(request):
    html = "index.html"
    empty_form = GhostPostForm()
    ghost_posts = GhostPost.objects.all()
    if request.method == "POST":
        form = GhostPostForm(request.POST)
        if form.is_valid():
            boast = form.cleaned_data.get("boast")
            text = form.cleaned_data.get("text")
            upvotes = 1
            downvotes = 0
            public_url = public_url_maker(text)
            private_url = private_url_maker(text)
            GhostPost.objects.create(
                boast=boast,
                text=text,
                upvotes=upvotes,
                downvotes=downvotes,
                public_url=public_url,
                private_url=private_url
            )
            return render(request, html, {"empty_form": empty_form, "ghost_posts": ghost_posts})

    return render(request, html, {"empty_form": empty_form, "ghost_posts": ghost_posts})