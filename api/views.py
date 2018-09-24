

# from elasticsearch import Elasticsearch, RequestsHttpConnection
# from rest_framework_elasticsearch import es_views, es_pagination, es_filters
# from api.elastic.indices.i_institution import InstitutionIndex
#
# class InstitutionView(es_views.ListElasticAPIView):
#     es_client = Elasticsearch(hosts=['localhost:9200/'],
#                               connection_class=RequestsHttpConnection)
#     es_model = InstitutionIndex
#     es_filter_backends = (
#         es_filters.ElasticFieldsFilter,
#         es_filters.ElasticSearchFilter
#     )
#     es_filter_fields = (
#         es_filters.ESFieldFilter('cert', 'name'),
#     )
#     es_search_fields = (
#         'cert',
#         'name'
#     )