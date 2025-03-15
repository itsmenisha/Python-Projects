from django.urls import path
from . import views

urlpatterns = [
    path("name/", views.todo, name="name"),
    path("clear-name/", views.clear_name, name="clear_name"),
    path("", views.task_list, name="index"),
]
