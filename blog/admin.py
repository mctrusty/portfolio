from django.contrib import admin
from .models import Blog

class CategoryAdmin(admin.ModelAdmin):
    pass

class BlogAdmin(admin.ModelAdmin)

admin.site.register(Blog, BlogAdmin)
admin.site.register(Category, CategoryAdmin)