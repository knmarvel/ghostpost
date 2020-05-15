from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="homepage"),
    path("ghostpost/<int:pk>/", views.ghostpost_public_detail, name="ghostpost_public_detail"),
    path("ghostpost/<str:private_url>/", views.ghostpost_private_detail, name="ghostpost_private_detail"),
    path("upvotes/<int:pk>/", views.upvote_view, name="upvotes"),
    path("downvotes/<int:pk>/", views.downvote_view, name="downvotes")
]