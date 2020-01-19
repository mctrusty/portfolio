from django.contrib import admin
from .models import Blog, Category

class CategoryAdmin(admin.ModelAdmin):
    pass

class BlogAdmin(admin.ModelAdmin):
    pass

admin.site.register(Blog, BlogAdmin)
admin.site.register(Category, CategoryAdmin)