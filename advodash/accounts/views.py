from django.shortcuts import render, redirect
from .forms import FirmUserLoginForm


# Create your views here.
def login(request):
    if request.method == "GET":
        context = {"form": FirmUserLoginForm()}
        print(context)
        return render(request, "registration/login.html", context=context)
    redirect('/')