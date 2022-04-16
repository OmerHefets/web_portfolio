from django.urls import path
from . import views

urlspatterns = [
    path("", views.blog_index, name="blog_index"),
    path("<category>/", views.blog_category, name="blog_category"),
    path("<int:pk>/", views.blog_detail, name="blog_detail"),
]