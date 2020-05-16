from django.shortcuts import render, reverse, HttpResponseRedirect
from datetime import datetime as dt
from posts.forms import GhostPostForm, SortForm
from posts.models import GhostPost, Sorter
from posts.helpers import private_url_maker


def index(request):
    html = "index.html"
    ghostpost_form = GhostPostForm()
    current_sort = Sorter.objects.first()
    ghost_posts = GhostPost.objects.all()
    if "boasts" in request.path:
        ghost_posts = ghost_posts.filter(boast=True)
    if "roasts" in request.path:
        ghost_posts = ghost_posts.filter(boast=False)
    sort_by = current_sort.sort_by
    sort_form = SortForm(initial={'sort_by': sort_by})
    if current_sort.sort_by == "new":
        ghost_posts = ghost_posts.order_by("-datetime")
    if current_sort.sort_by == "old":
        ghost_posts = ghost_posts.order_by("datetime")
    if current_sort.sort_by == "hot":
        ghost_posts = sorted(ghost_posts, key=lambda x: -x.score())
    if current_sort.sort_by == "not":
        ghost_posts = sorted(ghost_posts, key=lambda x: x.score())

    if request.method == "POST":
        if "sort_by" in request.POST:
            form = SortForm(request.POST)
            if form.is_valid():
                ghost_posts = GhostPost.objects.all()
                sort_by = form.cleaned_data.get("sort_by")
                current_sort.sort_by = sort_by
                current_sort.save()
                sort_by = current_sort.sort_by
                sort_form = SortForm(initial={'sort_by': sort_by})
                if current_sort.sort_by == "new":
                    ghost_posts = ghost_posts.order_by("-datetime")
                if current_sort.sort_by == "old":
                    ghost_posts = ghost_posts.order_by("datetime")
                if current_sort.sort_by == "hot":
                    ghost_posts = sorted(ghost_posts, key=lambda x: -x.score())
                if current_sort.sort_by == "not":
                    ghost_posts = sorted(ghost_posts, key=lambda x: x.score())
                return render(request, html, {"current_path": request.path, "sort_by": sort_by, "sort_form": sort_form, "ghostpost_form": ghostpost_form, "ghost_posts": ghost_posts})

        else:
            form = GhostPostForm(request.POST)
            if form.is_valid():
                boast = form.cleaned_data.get("boast")
                text = form.cleaned_data.get("text")
                upvotes = 0
                downvotes = 0
                private_url = private_url_maker()
                datetime = dt.now()
                GhostPost.objects.create(
                    boast=boast,
                    text=text,
                    upvotes=upvotes,
                    downvotes=downvotes,
                    private_url=private_url,
                    datetime=datetime
                )
                return render(request, html, {"current_path": request.path, "sort_by": sort_by, "sort_form": sort_form, "ghostpost_form": ghostpost_form, "ghost_posts": ghost_posts, "private_url": private_url})

    return render(request, html, {"current_path": request.path, "sort_by": sort_by, "sort_form": sort_form, "ghostpost_form": ghostpost_form, "ghost_posts": ghost_posts})


def ghostpost_public_detail(request, pk):
    html = "ghostpost_detail.html"
    ghostpost = GhostPost.objects.get(pk=pk)
    private = False
    return render(request, html, {"ghostpost": ghostpost, "private": private})


def ghostpost_private_detail(request, private_url):
    html = "ghostpost_detail.html"
    ghostpost = GhostPost.objects.get(private_url=private_url)
    private = True
    return render(request, html, {"ghostpost": ghostpost, "private": private})


def upvote_view(request, pk):
    post = GhostPost.objects.get(id=pk)
    post.upvotes += 1
    post.save()
    return HttpResponseRedirect(reverse("homepage"))


def downvote_view(request, pk):
    post = GhostPost.objects.get(id=pk)
    post.downvotes += 1
    post.save()
    return HttpResponseRedirect(reverse("homepage"))


def upvote_detail_view(request, pk):
    post = GhostPost.objects.get(id=pk)
    post.upvotes += 1
    post.save()
    return HttpResponseRedirect(reverse("ghostpost_public_detail", kwargs={"pk": pk}))


def downvote_detail_view(request, pk):
    post = GhostPost.objects.get(id=pk)
    post.downvotes += 1
    post.save()
    return HttpResponseRedirect(reverse("ghostpost_public_detail", kwargs={"pk": pk}))


def delete_post(request, private_url):
    deleted = GhostPost.objects.get(private_url=private_url).delete()
    return HttpResponseRedirect(reverse("homepage"))
