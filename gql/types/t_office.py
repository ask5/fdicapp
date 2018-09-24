from graphene_django.types import DjangoObjectType
from common.models.data_models.office import Office

class OfficeType(DjangoObjectType):
    class Meta:
        model = Office
