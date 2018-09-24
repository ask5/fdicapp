import graphene
from gql.types import OfficeType
from common.models.data_models.office import Office

class QueryOffice(graphene.ObjectType):
    office = graphene.Field(OfficeType,
                            uninum =graphene.Int(),
                            office_name=graphene.String())

    office_list = graphene.List(OfficeType)

    def resolve_office_list(self, info, **kwargs):
        return Office.objects.all()

    def resolve_office(self, info, **kwargs):

        uninum = kwargs.get('uninum')
        office_name = kwargs.get('office_name')

        if uninum is not None:
            return Office.objects.get(pk=uninum)

        if office_name is not None:
            return Office.objects.get(office_name=office_name)

        return None
