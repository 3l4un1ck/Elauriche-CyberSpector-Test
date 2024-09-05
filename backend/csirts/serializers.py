from rest_framework import serializers
from .models import CSIRT

class CSIRTSerializer(serializers.ModelSerializer):
    class Meta:
        model = CSIRT
        exclude = ('deleted', 'updated_at')