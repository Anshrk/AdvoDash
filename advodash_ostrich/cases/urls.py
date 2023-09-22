from django.urls import path

from . import views

urlpatterns = [
    path("", views.all_cases, name="all cases"),
    path("add/", views.add_case, name="add"),
]