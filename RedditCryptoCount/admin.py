from django.contrib import admin
from .models import LastCount, CheckedPosts

admin.site.register(LastCount)
admin.site.register(CheckedPosts)