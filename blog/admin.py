from django.contrib import admin
from .models import Blog, Category
from markdownx.admin import MarkdownxModelAdmin

class CategoryAdmin(admin.ModelAdmin):
    pass

class BlogAdmin(MarkdownxModelAdmin):
    pass

admin.site.register(Blog, MarkdownxModelAdmin)
admin.site.register(Category, CategoryAdmin)