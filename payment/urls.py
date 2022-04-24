from django.urls import path
from .import views

urlpatterns = [
    path('',views.checkout, name='checkout'),
    path('order',views.order, name='order'),
    path("payment_rzp", views.order_payment, name="payment_rzp"),
    path("callback", views.callback, name="callback"),
    
]
