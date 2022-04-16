from django.urls import path
from .import views


urlpatterns = [
    path('',views.product, name='products'),
    path('cart',views.cart, name='cart'),
    path('<str:slug>',views.product_detail, name='product-detail'),
    path('add-to-cart/<str:slug>',views.add_to_cart, name='add-to-cart'),
    path('add-to-cart/<str:slug>/<int:quantity>',views.add_to_cart, name='add-to-cart'),
    path('remove-cart-item/<str:slug>',views.remove_cart_item, name='remove-cart-item'),
    path('checkout/',views.checkout, name='checkout'),
    path('update-cart/',views.update_cart, name='update-cart')
]
