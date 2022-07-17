from django.contrib import admin

# Register your models here.
from .models import BlogModel, BlogUsers

admin.site.register(BlogModel)
admin.site.register(BlogUsers)