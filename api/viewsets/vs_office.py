from rest_framework import  viewsets
from common.models.data_models.office import Office
from api.serializers.ser_office import OfficeSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated


class OfficeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Office.objects.all()
    serializer_class = OfficeSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('cert', 'office_name')
    authentication_classes = (SessionAuthentication, )
    permission_classes = (IsAuthenticated,)
