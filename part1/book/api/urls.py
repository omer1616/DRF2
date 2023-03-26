from django.urls import path
from .views import book_list_api_view

urlpatterns = [
    path('book/', book_list_api_view, name='book-list'),
]
