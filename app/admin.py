from django.contrib import admin
from app.models import Categories, Post, Tags, Comments, Contact, About, Details

# Register your models here.

# It creates search filter, search field and what to display in admin panel
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'published', 'created_at', 'updated_at', 'category_id')
    list_filter = ('published', 'body')
    search_fields = ('title', 'body')
    

admin.site.register(Categories)
# admin.site.register(Post)
admin.site.register(Comments)
admin.site.register(Tags)
admin.site.register(Contact)
admin.site.register(About)
admin.site.register(Details)

