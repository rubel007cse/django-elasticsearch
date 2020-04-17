from django.contrib import admin

# Register your models here.
from .models import BlogPost, Article
# ...
#admin.site.register(Post)
admin.site.register(BlogPost)
admin.site.register(Article)