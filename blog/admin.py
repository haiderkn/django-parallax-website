from django.contrib import admin
from .models import BlogModel

# Register your models here.
admin.site.register(BlogModel)

class BlogModelAdmin(admin.ModelAdmin):
    list_display = ['date', 'writer', 'title', 'blog']