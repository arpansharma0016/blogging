from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('write/', views.write, name="write"),
    path('search/', views.search, name="search"),
    path('<str:title>-<int:post_id>/', views.post, name="post"),
]
