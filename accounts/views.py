from django.shortcuts import render, redirect
from accounts.forms import UserAdminCreationForm

# Create your views here.
def login(req):
    form = ()
    if req.method == 'POST':
        form = UserAdminCreationForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    return render(req, 'accounts/register.html', {'form': form})


# def register(req):
#     form = UserAdminCreationForm()
#     if req.method == 'POST':
#         form = UserAdminCreationForm(req.POST)
#         if form.is_valid():
#             form.save()
#         return redirect('/')
#     return render(req, 'registration/register.html', {'form': form})