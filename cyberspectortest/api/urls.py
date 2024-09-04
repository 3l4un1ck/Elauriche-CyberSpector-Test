from django.urls import path, include
from rest_framework.routers import DefaultRouter
from csirts.views import CSIRTViewSet

router = DefaultRouter()
router.register(r'csirts', CSIRTViewSet)

urlpatterns = [
    path('', include(router.urls)),
]