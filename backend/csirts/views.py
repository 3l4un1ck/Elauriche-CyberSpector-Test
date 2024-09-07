from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import CSIRT
from .serializers import CSIRTSerializer


class CSIRTViewSet(viewsets.ModelViewSet):
    queryset = CSIRT.objects.filter(deleted=False)
    serializer_class = CSIRTSerializer
    # permission_class = [permissions.IsAuthenticated]

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.deleted = True
        instance.save()
        return Response({'message': 'Instance deleted successfully'}, status=status.HTTP_204_NO_CONTENT)

    @action(detail=True, methods=['delete'], url_path='realDelete')
    def delete(self, request, pk=None):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
