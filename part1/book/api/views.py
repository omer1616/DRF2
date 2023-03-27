from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view

from ..models import Book
from .serializers import BookSerializer


@api_view(['GET', 'POST'])
def book_list_api_view(request):
    if request.method == 'GET':
        book = Book.objects.all()
        serializer = BookSerializer(book, many=True)  # many=True birder fazla queryset gönderince yazılır
        return Response(serializer.data)



    elif request.method == 'POST':
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def book_detail_api_view(request, pk):
    book = get_object_or_404(Book, pk=pk)

    if request.method == 'GET':
        serializer = BookSerializer(book)
        return Response(serializer.data)



    elif request.method == 'PUT':
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)


    elif request.method == 'DELETE':
        book.delete()
        return Response(
            {
                'işlem': {
                    'code': 204,
                    'message': f'({pk}) id numaralı makale silinmiştir.'
                }
            },
            status=status.HTTP_204_NO_CONTENT
        )
