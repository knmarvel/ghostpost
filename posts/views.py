from django.shortcuts import render, reverse, HttpResponseRedirect
from posts.forms import GhostPostForm
from posts.models import GhostPost
from posts.helpers import private_url_maker


def index(request):
    html = "index.html"
    empty_form = GhostPostForm()
    ghost_posts = GhostPost.objects.all()
    if request.method == "POST":
        form = GhostPostForm(request.POST)
        if form.is_valid():
            boast = form.cleaned_data.get("boast")
            text = form.cleaned_data.get("text")
            upvotes = 0
            downvotes = 0
            private_url = private_url_maker()
            GhostPost.objects.create(
                boast=boast,
                text=text,
                upvotes=upvotes,
                downvotes=downvotes,
                private_url=private_url
            )
            return render(request, html, {"empty_form": empty_form, "ghost_posts": ghost_posts, "private_url": private_url})

    return render(request, html, {"empty_form": empty_form, "ghost_posts": ghost_posts})


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
    return HttpResponseRedirect(reverse("ghostpost_public_detail", kwargs={"pk": pk}))


def downvote_view(request, pk):
    post = GhostPost.objects.get(id=pk)
    post.downvotes += 1
    post.save()
    return HttpResponseRedirect(reverse("ghostpost_public_detail", kwargs={"pk": pk}))


def delete_post(request, private_url):
    deleted = GhostPost.objects.get(private_url=private_url).delete()
    return HttpResponseRedirect(reverse("homepage"))

