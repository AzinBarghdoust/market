from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from settings.forms import ApiForm


@login_required
def settings(request):
    return render(request, 'settings.html')


@login_required
def api(request):
    if request.method == 'POST':
        form = ApiForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('trade')
    else:
        form = ApiForm()

    return render(request, 'api.html', context={'form': form})
