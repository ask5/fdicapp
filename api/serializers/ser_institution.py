from rest_framework import serializers
from common.models.data_models.institution import Institution


class InstitutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Institution
        fields = '__all__'
