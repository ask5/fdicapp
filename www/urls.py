from django.urls import path

from . import views

app_name = 'www'

urlpatterns = [
    path('', views.index, name='index'),
    path('pricing', views.pricing, name='pricing'),
    path('features', views.features, name='features'),
    path('privacy', views.privacy, name='privacy'),
    path('resources', views.resources, name='resources'),
    path('team', views.team, name='team'),
    path('terms', views.terms, name='terms'),
    path('support', views.support, name='support'),
    path('contact', views.contact, name='contact')
]
