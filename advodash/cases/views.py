from django.shortcuts import render
from .models import Cases

# Create your views here.

def index(request):
    return render(request, "cases/index.html")

def all_cases(request):
    context = {"cases" : Cases.objects.all()}
    return render(request, "cases/cases.html", context)