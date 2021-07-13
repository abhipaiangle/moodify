from django.urls import path
from . import views

urlpatterns = [
    path('pages/', views.index, name='index'),
    path('pages/auth', views.get_access_token, name='get_access'),

]