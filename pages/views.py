from django.shortcuts import render
from django.http import HttpResponse
from listings.choices import price_choices, state_choices

from listings.models import Listing
from proprietaire.models import proprietaire

def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]

    context = {
        'listings': listings,
        'state_choices': state_choices,
        'price_choices': price_choices
    }

    return render(request, 'pages/index.html', context)


def about(request):
    # Get all proprietaire
    proprietaires = proprietaire.objects.order_by('-hire_date')

    # Get MVP
    mvp_proprietaire= proprietaire.objects.all().filter(is_mvp=True)

    context = {
        'proprietaires': proprietaire,
        'mvp_proprietaires': mvp_proprietaire
    }

    return render(request, 'pages/about.html', context)