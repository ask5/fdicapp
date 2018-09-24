from rest_framework import routers
from api.viewsets import *

api_router = routers.DefaultRouter()
api_router.register(r'institutions', InstitutionViewSet)
api_router.register(r'offices', OfficeViewSet)