from ..models import Category, Product
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.mixins import (ListModelMixin,
                                   CreateModelMixin,
                                   RetrieveModelMixin,
                                   UpdateModelMixin,
                                   DestroyModelMixin)
from .serializer import CategorySerializer, ProductSerializer
from rest_framework.generics import GenericAPIView


# class ListCreateCategory(GenericAPIView):
#     serializer_class = CategorySerializer
#     queryset = Category.objects.all()
#
#     def get(self, request, *args, **kwargs):
#         instance = self.get_object()
#         serializer = self.get_serializer(instance)
#         return Response(serializer.data)
#
#     def delete(self, request, *args, **kwargs):
#         instance = self.get_object()
#         instance.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


class ListCreateCategory(ListModelMixin, CreateModelMixin, GenericAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

    # listelemek
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    # yaratmak istiyorum
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class RetrieveUpdateDestroy(RetrieveModelMixin,
                            UpdateModelMixin,
                            DestroyModelMixin,
                            GenericAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class ListCreateProduct(ListModelMixin, CreateModelMixin, GenericAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    # listelemek
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    # yaratmak istiyorum
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
