from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from accounts.forms import UserAdminCreationForm


def signup(req):
    form = UserAdminCreationForm()
    if req.method == 'POST':
        form = UserAdminCreationForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('signup')
    return render(req, 'registration/signup.html', {'form': form})


