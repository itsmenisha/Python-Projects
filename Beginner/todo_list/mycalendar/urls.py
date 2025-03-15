from django.urls import path
from . import views

urlpatterns = [
    path('', views.mycalendar, name='calander'),
]
