from django.urls import path

from . import views

app_name = 'common'

urlpatterns = [
    path('sign_up', views.sign_up, name='sign_up'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('unauthorized', views.unauthorized, name='unauthorized'),
]
