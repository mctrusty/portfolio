from django.urls import path
from . import views

urlpatterns = [
    path('', views.allblogs, name='allblogs'),
    path('<int:blog_id>/', views.detail, name='blog_detail'),
    path('<category>', views.category, name="blog_category")
]