from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.shortcuts import render
import requests
from settings.forms import ApiForm


@login_required
def settings(request):
    return render(request, 'settings.html')


@login_required
def api(request):
    form = ApiForm()
    if request.method == 'POST':
        form = ApiForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('trade')
    else:
        form = ApiForm()

    return render(request, 'api.html', context={'form': form})


def trade(request):
    url_coin = "https://api.kucoin.com/api/v1/symbols"
    response = requests.get(url=url_coin).json()
    data = response['data']
    for i in range(len(data)):
        mark = response['data'][i]['market']
        base = response['data'][i]['baseCurrency']
        quote = response['data'][i]['quoteCurrency']
        # base_currency = response['data'][i]['baseCurrency']
        # print(base_currency)
    return render(request, 'trade.html', context={'market': mark, 'base': base, 'quote': quote})
