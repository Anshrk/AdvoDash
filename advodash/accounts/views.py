from django.shortcuts import render
from .forms import FirmAuthenticationForm


# Create your views here.
def login(request):

    if request.method == "POST":
        ...

def register(request):
    if request.method == "GET":
        context = {
            "form": FirmAuthenticationForm()
        }
        return render(request, 'authentication/register.html', context=context)
    ...
    