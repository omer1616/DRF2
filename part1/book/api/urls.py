from django.urls import path
from .views import BookListCreateApiView, BookDetailApiView, AuthorListCreateApiView

urlpatterns = [
    path('book/', BookListCreateApiView.as_view(), name='book-list'),
    path('book/<int:pk>/', BookDetailApiView.as_view(), name='book-detail'),
    path('author/', AuthorListCreateApiView.as_view(), name='author-list'),
]
