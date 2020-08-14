from django.urls import path
from . import views

app_name = 'dev'

urlpatterns = [
    path('', views.RequestList.as_view(), name='req_list')
]