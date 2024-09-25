# listings/views.py

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core .mail import send_mail
from listings.models import Band
from listings.models import Title
from listings.forms import ContactUsForm


def band_create(request):
    return render(request, 'listings/band_create')

def band_list(request):
    bands = Band.objects.all()
    return render(request,
                  'listings/band_list.html',
                  {'bands':bands})

def band_detail(request, id):
    band = Band.objects.get(id=id)
    return render(request,
                  'listings/band_detail.html',
                  {'band': band},)

def listings_list(request):
    titles = Title.objects.all()
    return render(request,
                  'listings/listings_list.html',
                  {'titles':titles})

def listings_detail(request,id):
    title = Title.objects.get(id=id)
    return render(request,
                  'listings/listing_detail.html',
                  {'titles':title})

def about(request):
    return render(request,'listings/about.html')

def contact(request):
    if request.method == 'POST':
        form = ContactUsForm(request.POST)

        if form.is_valid():
            send_mail(
                subject= f'message from {form.cleaned_data['name'] or 'anonyme'} via Merchex Contact Us form',
                message= form.cleaned_data['message'],
                from_email = form.cleaned_data['email'],
                recipient_list= ['admin@merchex.xyz']
            )
            return redirect('email sent')

    else:
        form = ContactUsForm()
    return render(request,
                  'listings/contact.html',
                  {'form': form})
