from django.template import loader
from django.shortcuts import render, redirect
from .models import Case, CaseStage, CaseType
from .forms import CaseForm

# Create your views here.
def all_cases(request):
    context = {"cases" : Case.objects.all()}
    return render(request, "cases/index.html", context)

def add_case(request):
    form = CaseForm()

    if request.method == "POST":
        form = CaseForm(request.POST)
        if form.is_valid():
            form.save()

    context = {"form": form}
    return render(request, "cases/add_case.html", context)