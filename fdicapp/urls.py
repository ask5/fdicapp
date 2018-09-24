"""fdicapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from graphene_django.views import GraphQLView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('www/', include('www.urls')),
    path('api/', include('api.urls')),
    path('els/', include('elastic.urls')),
    path('web/', include('web.urls')),
    path('sys/', include('common.urls')),
    path('m/', include('mobile.urls')),
    path('prv/', include('provisioning.urls')),
    path('gql/', GraphQLView.as_view(graphiql=True)),
    path('', lambda r: redirect('www:index')),
]
