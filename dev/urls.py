from django.urls import path
from . import views

app_name = 'dev'

urlpatterns = [
    path('', views.Top.as_view(), name='top'),
    path('request/', views.RequestList.as_view(), name='request_list')
]