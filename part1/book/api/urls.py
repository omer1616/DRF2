from django.urls import path
from .views import book_list_api_view,book_detail_api_view

urlpatterns = [
    path('book/', book_list_api_view, name='book-list'),
    path('book/<int:pk>/', book_detail_api_view, name='book-detail'),
]
