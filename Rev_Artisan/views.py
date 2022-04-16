from cgitb import html
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def home_p(request):
    return render(request,'Rev_Artisan/home.html')

@login_required
def about_p(request):
    return render(request,'Rev_Artisan/about.html')

@login_required
def contact_p(request):
    
    return render(request,'Rev_Artisan/contact.html')
    
@login_required
def product_p(request):
    return render(request,'Rev_Artisan/product.html')