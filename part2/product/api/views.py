from ..models import Category, Product
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework import mixins
from .serializer import CategorySerializer, ProductSerializer
from rest_framework import generics


# class ListCreateCategory(generics.ListCreateAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer

class ListCreateCategory(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

    # listelemek
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    # yaratmak istiyorum
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class RetrieveUpdateDestroyCategory(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ListCreateProduct(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ListProductOfCategory(generics.ListAPIView):

    serializer_class = ProductSerializer

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        return Product.objects.filter(category_id=pk)





class ListCreateCategoryGen(generics.GenericAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

    def get(self, request, *args, **kwargs):
        instance = self.get_queryset()
        serializer = self.get_serializer(instance, many=True)
        return Response(serializer.data)






