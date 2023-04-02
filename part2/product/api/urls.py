from django.urls import path
from .views import ListCreateCategory, ListCreateProduct, RetrieveUpdateDestroyCategory, ListProductOfCategory

urlpatterns = [
    path('category/', ListCreateCategory.as_view(),  name="list-create-category"),
    path('category/<int:pk>', RetrieveUpdateDestroyCategory.as_view(),  name="retrive-update-delete"),
    path('category/<int:pk>/products', ListProductOfCategory.as_view(),  name="retrive-update-delete"),
    path('product/', ListCreateProduct.as_view(),  name="list-create-product")
    # path('<int:pk>', ListCreateCategory.as_view(),  name="list-create-category")

]