from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from ..models import Book
from .serializers import BookSerializer


@api_view(['GET'])
def book_list_api_view(request):
    book = Book.objects.all()
    serializer = BookSerializer(book, many=True)
    return Response(serializer.data)



