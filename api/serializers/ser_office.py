from rest_framework import serializers
from common.models.data_models.office import Office

class OfficeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Office
        fields = '__all__'
