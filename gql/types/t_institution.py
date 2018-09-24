from graphene_django.types import DjangoObjectType
from common.models.data_models.institution import Institution

class InstitutionType(DjangoObjectType):
    class Meta:
        model = Institution
