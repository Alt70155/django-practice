from django.urls import path
from . import views

app_name = 'diaries'

urlpatterns = [
  path('', views.top, name='top')
]