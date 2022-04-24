from ast import Delete
from multiprocessing import context
from django.shortcuts import render,redirect
from products.models import Cart
from project_z.settings import RAZORPAY_API_KEY, RAZORPAY_API_SECRET_KEY 
from .models import Delivery_Details, Order
import razorpay
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
from .utils import cart_total, rupee_to_paisa
from products.utils import cart_total_item
from .constants import PaymentStatus
import json

# Create your views here.
def order(request):
    return render(request,'Rev_Artisan/order.html')

client = razorpay.Client(auth=('rzp_test_0Yt8PmMs4GMGQy','DnD2DY0DToIMeHpgpUTZMpKz'))
def checkout(request):
    if request.method == "GET":
        if not request.user.is_authenticated:
            return redirect('login')
        cart = Cart.objects.filter(user=request.user)
        cart_total_value = cart_total(cart)
        payment = client.order.create({'amount':rupee_to_paisa(cart_total_value),'currency':'INR','payment_capture':'1' })
        try:
            delivery_details = Delivery_Details.objects.get(user=request.user)
        except:
            delivery_details = None

        print(payment)
        context = {
            'cart':cart,
            'total':cart_total_value,    
            'payment':payment,
            'delivery_details': delivery_details
        }

        return  render(request, 'Rev_Artisan/checkout.html', context)
    return render(request,'Rev_Artisan/checkout.html')
    # return render(request,'Rev_Artisan/checkout.html',context)
    





def order_payment(request):
    if request.method == "POST":
        phno = request.POST.get('phno')
        address = request.POST.get('address')
        country = request.POST.get('country')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zip = request.POST.get('zip')
        total_amt = rupee_to_paisa(int(request.POST.get('totamt'))) 
        
        delivery_details, created = Delivery_Details.objects.get_or_create(user=request.user, pincode=zip)
        delivery_details.phno = phno
        delivery_details.address = address
        delivery_details.country = country
        delivery_details.city = city
        delivery_details.state = state
        # delivery_details.pincode = zip
        delivery_details.save()
        
        name = request.user.get_full_name()
        amount = request.POST.get('totamt')
        client = razorpay.Client(auth=(RAZORPAY_API_KEY, RAZORPAY_API_SECRET_KEY))
        razorpay_order = client.order.create(
            {"amount": int(amount) * 100, "currency": "INR", "payment_capture": "1"}
        )
        order = Order.objects.create(
            name=name, user=request.user, amount=amount, provider_order_id=razorpay_order["id"]
        )
        order.save()
        return render(
            request,
            "Rev_Artisan/payment.html",
            {
                "callback_url": "http://" + "127.0.0.1:8000" + reverse('callback'),
                "razorpay_key": RAZORPAY_API_KEY,
                "order": order,
                "user": request.user,
                "phone_number": phno,
                "delivery_address": delivery_details,
            },
        )
    return render(request, "Rev_Artisan/payment.html")


@csrf_exempt
def callback(request):
    def verify_signature(response_data):
        client = razorpay.Client(auth=(RAZORPAY_API_KEY, RAZORPAY_API_SECRET_KEY))
        return client.utility.verify_payment_signature(response_data)

    if "razorpay_signature" in request.POST:
        payment_id = request.POST.get("razorpay_payment_id", "")
        provider_order_id = request.POST.get("razorpay_order_id", "")
        signature_id = request.POST.get("razorpay_signature", "")
        order = Order.objects.get(provider_order_id=provider_order_id)
        order.payment_id = payment_id
        order.signature_id = signature_id
        order.save()
        if not verify_signature(request.POST):
            order.status = PaymentStatus.FAILURE
            order.save()

            return render(request, "Rev_Artisan/callback.html", context={"status": order.status})
        else:
            order.status = PaymentStatus.SUCCESS
            order.save()
            cart = Cart.objects.filter(user=order.user)
            cart.delete()
            return render(request, "Rev_Artisan/callback.html", context={"status": order.status})
    else:
        payment_id = json.loads(request.POST.get("error[metadata]")).get("payment_id")
        provider_order_id = json.loads(request.POST.get("error[metadata]")).get(
            "order_id"
        )
        order = Order.objects.get(provider_order_id=provider_order_id)
        order.payment_id = payment_id
        order.status = PaymentStatus.FAILURE
        order.save()
        return render(request, "Rev_Artisan/callback.html", context={"status": order.status})