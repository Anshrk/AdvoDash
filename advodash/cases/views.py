from django.template import loader
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Case, CaseStage, CaseType
from .forms import CaseForm

# Create your views here.
@login_required(login_url="/accounts/login")
def index(request):
    context = {
        "nothing": ['1', '2']
    }
    template = loader.get_template("cases/index.html")
    return render(request, "cases/index.html", context)

def add_case(request):
    form = CaseForm()

    if request.method == "POST":
        form = CaseForm(request.POST)
        if form.is_valid():
            form.save()

    context = {"form": form}
    return render(request, "cases/add_case.html", context)