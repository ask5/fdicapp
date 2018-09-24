import graphene
from gql.queries import QueryInstitution, QueryOffice


class Query(QueryInstitution, QueryOffice,
            graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query)
