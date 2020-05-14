from django.contrib import admin

# Register your models here.
from posts.models import GhostPost
admin.site.register(GhostPost)