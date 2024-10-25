from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.db import models
from .models import Featured_Products,Latest_Products
from .forms import NewsletterForm


# Create your views here.

def index(request):
    newsletterform = NewsletterForm()
    context ={
             'featuredproducts':Featured_Products.objects.all(),
             'latestproducts': Latest_Products.objects.all(),
             "newsletterform": newsletterform,
    }
    if request.method == "POST":
        newsletterform = NewsletterForm(request.POST)
        
    if newsletterform.is_valid():
            email = newsletterform.cleaned_data["email"]
            newsletterform.save()
            return redirect('subscribe')
    else:
            newsletterform = NewsletterForm()
                 
 
    return render(request, "index.html", context)

def subscribe(request):
    return render(request, "subscribe.html")

    

def products(request):
    return render(request, "product-listing.html")

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")

def cart(request):
    return render(request, "cart.html")

def checkout(request):
    return render(request, "checkout.html")

