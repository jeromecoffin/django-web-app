from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band
from listings.models import Listing

def hello(request):
    bands = Band.objects.all()
    return render(request, 'listings/hello.html',
        {'bands': bands})

def listings(request):
    lists = Listing.objects.all()
    return render(request, 'listings/listings.html',
        {'lists': lists})

def about(request):
    return render(request, 'listings/about.html')

def contact(request):
    return render(request, 'listings/contact.html')