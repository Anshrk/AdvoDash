from django.urls import path
from django.contrib.auth import views as auth_views
from .views import login

# from .views import UserView, signup

urlpatterns = [
    path("login/", login, name="login"),
    # path("login/", views.add_case, name="add"),
]