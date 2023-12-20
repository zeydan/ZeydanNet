from django.shortcuts import render
from .models import Portfolio, PortfolioFilter

# Create your views here.

def portfolio(request):
    return render(request, 'gallery.html', {
        'pagetitle' : 'Portfolio',
        'filters' : PortfolioFilter.objects.all(),
        'cards' : Portfolio.objects.all()
    })

def detail(request, name):
    return render(request, 'detail.html',{
        'redirect' : 'portfolio',
        'detail' : Portfolio.objects.get(unique_title = name)
    })
