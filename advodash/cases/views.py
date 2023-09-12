from django.template import loader
from django.shortcuts import render
from .models import Case, CaseStage, CaseType
from .forms import CaseForm

# Create your views here.
def index(request):
    context = {
        "nothing": ['1', '2']
    }
    template = loader.get_template("cases/index.html")
    return render(request, "cases/index.html", context)

def add_case(request):
    form = CaseForm()
    context = {"form": form}
    return render(request, "cases/add_case.html", context)