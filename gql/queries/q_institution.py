import graphene
from gql.types import InstitutionType
from common.models.data_models.institution import Institution


class QueryInstitution(graphene.ObjectType):
    institution = graphene.Field(InstitutionType,
                              cert=graphene.Int(),
                              name=graphene.String())

    institution_list = graphene.List(InstitutionType)

    def resolve_institution_list(self, info, **kwargs):
        return Institution.objects.filter(active=True).all()

    def resolve_institution(self, info, **kwargs):

        cert = kwargs.get('cert')
        name = kwargs.get('name')

        if cert is not None:
            return Institution.objects.get(pk=cert)

        if name is not None:
            return Institution.objects.get(name=name)

        return None
