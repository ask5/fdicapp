from django.urls import path

from . import views

app_name = 'elastic'

urlpatterns = [
    path('institutions', views.Institution, name='institutions'),
    path('offices', views.Office, name='offices'),
]
