from django.urls import path
from .views import ListCreateCategory, ListCreateProduct, RetrieveUpdateDestroy

urlpatterns = [
    path('category/', ListCreateCategory.as_view(),  name="list-create-category"),
    path('category/<int:pk>', RetrieveUpdateDestroy.as_view(),  name="retrive-update-delete"),
    path('product/', ListCreateProduct.as_view(),  name="list-create-product")
    # path('<int:pk>', ListCreateCategory.as_view(),  name="list-create-category")

]