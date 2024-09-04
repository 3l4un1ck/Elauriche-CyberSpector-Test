from rest_framework import viewsets
from .models import CSIRT
from .serializers import CSIRTSerializer

class CSIRTViewSet(viewsets.ModelViewSet):
    queryset = CSIRT.objects.filter(deleted=False)
    serializer_class = CSIRTSerializer