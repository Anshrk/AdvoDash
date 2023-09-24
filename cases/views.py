from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView


from .models import Cases
from .forms import CaseForm

# Create your views here.

@method_decorator(login_required, name="dispatch")
class CaseView(ListView):
    model = Cases

    template_name = 'cases/cases.html'
    list_display = ("case_id")
    



def index(request):
    return render(request, "cases/index.html")

# @login_required()
# def all_cases(request):
#     context = {"cases" : Cases.objects.all()}
#     return render(request, "cases/cases.html", context)

@login_required()
def add_case(request):
    form = CaseForm()

    if request.method == "POST":
        form = CaseForm(request.POST)
        if form.is_valid():
            form.save()
            redirect('/cases')

    context = {"form": form}
    return render(request, "cases/add_case.html", context)
