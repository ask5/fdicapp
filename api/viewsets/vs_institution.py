from rest_framework import  viewsets
from rest_framework import filters
from common.models.data_models.institution import Institution
from api.serializers.ser_institution import InstitutionSerializer
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated

class InstitutionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Institution.objects.all()
    serializer_class = InstitutionSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('cert', 'name')
    authentication_classes = (SessionAuthentication, )
    permission_classes = (IsAuthenticated,)


