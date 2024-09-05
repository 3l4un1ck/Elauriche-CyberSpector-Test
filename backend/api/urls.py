from django.urls import path, include
from users.views import UserViewSet
from rest_framework.routers import DefaultRouter
from csirts.views import CSIRTViewSet

router = DefaultRouter()
router.register(r'csirts', CSIRTViewSet)
router.register(r'user', UserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls)),
]