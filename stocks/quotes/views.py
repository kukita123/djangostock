from django.shortcuts import render, redirect
from .models import Stock
from django.contrib import messages
from .forms import StockForm

# Create your views here.

# pk_1713fe715ca944f996f6fbb51ce21314


def home(request):
    import requests
    import json

    if request.method == 'POST':
        ticker = request.POST['ticker']
        # pk_1713fe715ca944f996f6fbb51ce21314
        api_request = requests.get(
            # "https://api.iex.cloud/v1/data/core/quote/aapl?token=pk_1713fe715ca944f996f6fbb51ce21314")
            "https://cloud.iexapis.com/stable/stock/" + ticker + "/quote?token=pk_1713fe715ca944f996f6fbb51ce21314")

        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = "Error..."
        return render(request, 'home.html', {'api': api})

    else:
        return render(request, 'home.html', {'ticker': "Enter a Ticker Symbol Above ..."})


def about(request):
    return render(request, 'about.html', {})


def add_stock(request):
    if request.method == 'POST':
        form = StockForm(request.POST or None)

        if form.is_valid():
            form.save()
            messages.success(request, ("Stock Has Benn Added"))
            return redirect('add_stock')

    else:

        ticker = Stock.objects.all()
        return render(request, 'add_stock.html', {})
