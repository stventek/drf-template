from django.contrib import admin
from apps.example_app.models import *
# Register your models here.
admin.site.register(Author)
admin.site.register(BlogPost)