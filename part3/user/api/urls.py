from django.urls import path
from .views import ProfileViewSet, UserViewSet
from rest_framework.routers import DefaultRouter, SimpleRouter
"""profile_list = ProfileViewSet.as_view({'get': 'list'})
profile_detail = ProfileViewSet.as_view({'get': 'retrieve'})

urlpatterns = [
    path('profile/', profile_list, name='profile_list'),
    path('profile/<int:pk>', profile_detail, name='profile_detail')
]
"""




router = DefaultRouter()

router.register(r'profile', ProfileViewSet, basename='profil')
router.register(r'user', UserViewSet, basename='user')
urlpatterns = router.urls