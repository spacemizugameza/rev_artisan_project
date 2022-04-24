from atexit import register
from django.shortcuts import render, redirect
from django.contrib import messages

from .models import Cart, Product, Category,User
from django.contrib.auth.decorators import login_required
from payment.utils import cart_total
from .utils import cart_total_item
# Create your views here.
@login_required
def product(request, category_slug=None):
    if request.method == 'GET':
        context = {}
        products = None
        # if category_slug:
        #     categories = Category.objects.filter(slug=category_slug)
        #     for category in categories:
        #         products += Product.objects.filter(category=category)
        # else:
        products = Product.objects.all()
        context['products'] = products
       
        return  render(request, 'Rev_Artisan/product.html', context)

@login_required
def product_detail(request, slug):
    if request.method == 'GET':
        # print("P-slug:", slug)
        context = {}
        product = Product.objects.get(slug=slug)
        context['product'] = product
        return  render(request, 'Rev_Artisan/product_details.html', context)

@login_required
def add_to_cart(request, slug, quantity=1):
    if request.method == 'GET':
        print(":::Cart:", slug, quantity)
        print(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
        context = {}
        product = Product.objects.get(slug=slug)
        if product.quantity > quantity:
            cart_item, created = Cart.objects.get_or_create(product=product, user=request.user)
            print(cart_item)
            cart_item.quantity = 1 if created else cart_item.quantity + 1
            cart_item.save()


            messages.success(request, 'Product Successfully added to cart.')
        else:
            messages.error(request, 'Product is not in stock.')
        request.session['cart_total'] = cart_total_item(request.user)
        return  redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))

@login_required
def cart(request):

    if request.method == 'GET':
        cart = Cart.objects.filter(user=request.user)
        cart_total_value = cart_total(cart)        

        context = {
            'cart':cart,
            'total':cart_total_value,
            
        }

        return  render(request, 'Rev_Artisan/cart.html', context)
    request.session['cart_total'] = cart_total_item(request.user)
    return  redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))

def remove_cart_item(request,slug):
    print(slug)
    product = Product.objects.get(slug=slug)
    if product:
        cart = Cart.objects.filter(product_id=product.id, user=request.user)
        if cart:
            cart.delete()
            messages.success(request, 'item deleted from cart')
        else:
            messages.error(request, 'Somethign went wrong')
    else:
        messages.error(request, "something went wrong!")
    request.session['cart_total'] = cart_total_item(request.user)
    return  redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))

def update_cart(request):
    print(request.POST)
    if request.method == 'POST':
        print(request.POST)
        quantity = request.POST.get('quantity')
        cartid = request.POST.get('id')
        print(quantity)
        print(cartid)

        cart = Cart.objects.get(id=cartid)
            
        cart.quantity = int(quantity)
        cart.save()
    request.session['cart_total'] = cart_total_item(request.user)
    return  redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
    # return  render(request, 'Rev_Artisan/cart.html', context)
    



# def checkout(request):

#      if request.method == 'GET':
#         cart = Cart.objects.filter(user=request.user)
#         cart_total=0
#         context = {}
        

        
#         for c in cart:
#             cart_total += c.total
        

#         context = {
#             'cart':cart,
#             'total':cart_total
#         }


#         return render(request,'Rev_Artisan/checkout.html',context)
    




        
    





