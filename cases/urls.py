from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="Home Page"),
    path("add/", views.add_case, name="add"),
    path("cases/", views.CaseView.as_view(), name="List Cases"),
]