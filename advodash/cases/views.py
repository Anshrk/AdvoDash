from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Cases
from .forms import CaseForm
# Create your views here.

def index(request):
    return render(request, "cases/index.html")

@login_required()
def all_cases(request):
    context = {"cases" : Cases.objects.all()}
    return render(request, "cases/cases.html", context)

@login_required()
def add_case(request):
    form = CaseForm()

    if request.method == "POST":
        form = CaseForm(request.POST)
        if form.is_valid():
            form.save()

    context = {"form": form}
    return render(request, "cases/add_case.html", context)
