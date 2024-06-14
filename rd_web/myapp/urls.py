# myapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.book_list, name='book_list'),
    path('parent_titles/', views.parent_title_list, name='parent_title_list'),
    path('parent_titles/<int:parent_id>/', views.parent_title_detail, name='parent_title_detail'),
]