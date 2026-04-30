from django.contrib import admin
from app.models import Categories
from app.models import Post
from app.models import Comments

# Register your models here.
admin.site.register(Categories)
admin.site.register(Post)
admin.site.register(Comments)
